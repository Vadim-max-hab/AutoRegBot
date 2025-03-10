import random
import requests
import string
from config import TEMP_MAIL_API, SMS_SERVICES

def get_temp_email():
    """Получаем временную почту с API"""
    response = requests.get(TEMP_MAIL_API)
    return response.json()["email"]

def get_sms_code(phone_number=None):
    """Получаем номер телефона и SMS-код"""
    for service_name, api_url in SMS_SERVICES.items():
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if phone_number:
                return data["sms_code"]
            return data["phone"], service_name

    return None, None

def generate_random_name():
    """Генерируем случайное имя"""
    return "".join(random.choices(string.ascii_letters, k=8))
