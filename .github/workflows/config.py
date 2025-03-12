# API для временной почты
TEMP_MAIL_API = "https://www.1secmail.com/api/v1/?action=genRandomMailbox"

# API для SMS-активации
SMS_SERVICES = {
    "sms-activate": "https://sms-activate.org/stubs/handler_api.php?api_key=ВАШ_КЛЮЧ&action=getNumber",
    "5sim": "https://5sim.net/v1/user/getNumber?api_key=ВАШ_КЛЮЧ"
}

# Список сервисов для регистрации
SERVICES = {
    "Telegram": {
        "register_url": "https://my.telegram.org/auth/send_password",  # Пример URL для Telegram
        "confirm_url": "https://my.telegram.org/auth/login"          # Пример URL для подтверждения
    },
    "Google": {
        "register_url": "https://accounts.google.com/signup/v2",     # Актуальный URL для регистрации
        "confirm_url": "https://accounts.google.com/signup/v2/confirm"
    },
    "BTCPay": {
        "register_url": "https://btcpayserver.org/account/register", # Актуальный URL для регистрации
        "confirm_url": "https://btcpayserver.org/account/confirm"   # Актуальный URL для подтверждения
    }
}

# Прокси для анонимности
PROXIES = {
    "http": "socks5://127.0.0.1:9050",  # Локальный прокси (например, Tor)
    "https": "socks5://127.0.0.1:9050"
}​
