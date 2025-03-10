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
        "register_url": "https://telegram.org/api/register",
        "confirm_url": "https://telegram.org/api/confirm"
    },
    "Google": {
        "register_url": "https://accounts.google.com/signup",
        "confirm_url": "https://accounts.google.com/verify"
    },
    "BTCPay": {
        "register_url": "https://btcpayserver.org/signup",
        "confirm_url": "https://btcpayserver.org/confirm"
    }
}

# Прокси для анонимности
PROXIES = {
    "http": "socks5://127.0.0.1:9050",
    "https": "socks5://127.0.0.1:9050"
}
