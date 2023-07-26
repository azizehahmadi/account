from django.core.mail import EmailMessage
import os

class Utile:

    @staticmethod
    def send_email(data):
       try:
           email = EmailMessage(
               subject=data['subject'],
               body=data['body'],
               from_email=os.environ.get('EMAIL_FROM'),
               to=[data['to_email']]
           )
           email.send()
       except Exception as e:
           print("خطا در ارسال ایمیل", e)
