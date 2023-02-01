from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from venom.celery_task import app


def send_otp_to_phone_number(phone_number):
    pass


@app.task
def send_mail(subject='Test Mail', to='', body='', html_template=None, context={}):
    html_page = render_to_string(template_name=html_template, context=context)
    email = EmailMultiAlternatives(
        subject=subject,
        from_email=settings.EMAIL_HOST_USER,
        to=to,
        body=body
    )
    email.attach_alternative(content=html_page, mimetype='text/html')
    email.send()
