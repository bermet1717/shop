from django.core.mail import send_mail


def send_confirmation_email(code, email):
    full_link = f'http://localhost:8000/account/activate/{code}'


    send_mail(
        'Hello',
        full_link,
        [email]
    )