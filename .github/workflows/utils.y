import random
import requests
import string
from config import TEMP_MAIL_API, SMS_SERVICES

def get_temp_email():
    """Получаем временную почту с API"""
    try:
        response = requests.get(TEMP_MAIL_API)
        response.raise_for_status()  # Проверяем, что запрос успешен
        return response.json()["email"]
    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка при получении временной почты: {e}")
        return None

def get_sms_code(phone_number=None):
    """Получаем номер телефона и SMS-код"""
    for service_name, api_url in SMS_SERVICES.items():
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Проверяем, что запрос успешен
            data = response.json()

            if phone_number:
                # Если передан номер, возвращаем SMS-код
                if "sms_code" in data:
                    return data["sms_code"]
            else:
                # Если номер не передан, возвращаем номер и имя сервиса
                if "phone" in data:
                    return data["phone"], service_name

        except requests.exceptions.RequestException as e:
            print(f"❌ Ошибка при запросе к сервису {service_name}: {e}")

    return None, None

def generate_random_name(length=8):
    """Генерируем случайное имя"""
    return "".join(random.choices(string.ascii_letters, k=length))
​
