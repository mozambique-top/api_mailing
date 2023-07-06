import logging
import time
import sys
import requests
from django.utils import timezone
from config.wsgi import *
from mailings.models import Contact, Mailing, Message

logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s  %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.ERROR
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

RETRY_TIME = 10
TIME_FORMAT = "%Y-%m-%d - %H:%M:%S"
SENDING_API_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTkzMzA4OTQsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9NZWwxb2Rhc3UifQ.y1-NlIh5o0lClgztG3TkwwyLQGs4La2PdmRdOs1QTfk'


class MissingValueException(Exception):
    """Создаем свое исключения при отсутствии переменных окружения."""


class GetAPIException(Exception):
    """Создаем свое исключение при сбое запроса к API отправки сообщений."""


def send_api_message(message_id, contact, message):
    """Отправляем сообщение через внешнее API"""
    headers = {'Authorization': f'Bearer {SENDING_API_TOKEN}'}
    json = {
        "phone": contact,
        "text": message
    }
    try:
        response = requests.post(
            f'https://probe.fbrq.cloud/v1/send/{message_id}'.format(
                message_id=message_id
            ),
            headers=headers,
            json=json
        )
        logger.info('Сообщение отправлено через венешний API')
        return response.status_code == 200
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения: {error}')
        return False


def start_mailings():
    """Основной код обработки рассылок."""
    logger.info('-----------------')
    message_id = [1]
    finished_mailing_id = []
    if SENDING_API_TOKEN is None:
        raise MissingValueException('Отсутствуют переменные окружения!')
    while True:
        try:
            logger.info('Начало новой итерации')
            current_datetime = timezone.now()
            mailings = Mailing.objects.filter(
                start_send_time__lte=current_datetime,
                end_send_time__gte=current_datetime
            ).exclude(id__in=finished_mailing_id)

            for mailing in mailings:
                mailing_id = mailing.id
                tag = mailing.tag
                code = mailing.code
                text = mailing.text
                contacts = Contact.objects.filter(tag=tag, code=code)

                for contact in contacts:
                    contact_id = contact.id
                    if current_datetime <= mailing.end_send_time and send_api_message(
                            message_id[0],
                            contact.number,
                            text
                    ):
                        Message.objects.create(
                            status='S',
                            mailing_id=mailing_id,
                            contact_id=contact_id
                        )
                    else:
                        Message.objects.create(
                            status='N',
                            mailing_id=mailing_id,
                            contact_id=contact_id
                        )
                    message_id[0] += 1
                finished_mailing_id.append(mailing_id)
            logger.info('Конец итерации')
            logger.info('-----------------')
            time.sleep(RETRY_TIME)

        except Exception as error:
            logger.error(f'Сбой в работе программы: {error}')
            logger.info('-----------------')
            time.sleep(RETRY_TIME)

