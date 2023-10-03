from django_mailer import send_mail
from .models import Bulletin

def send_newsletter(subject, message):
    bulletins = Bulletin.objects.all()
    for bulletin in bulletins:
        send_mail(
            subject,
            message,
            'noreply@example.com',  # Замените на ваш адрес электронной почты
            [bulletin.user.email],
            fail_silently=False,
        )
