from users.models import EmailVerifyRecord
from django.core.mail import send_mail
import random
import string

def random_str(randomLength=8):
    chars = string.ascii_letters + string.digits
    strcode=''.join(random.sample(chars,randomLength))
    return strcode

def send_register_email(email, send_type='register'):
    email_record= EmailVerifyRecord()
    code = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = 'Blog register verification.'
        email_body= 'Click to activate your account: http://127.0.0.1:8000/users/active/{0}'.format(code)
        send_status=send_mail(email_title, email_body, 'lwh7749@outlook.com',[email])
        if send_status:
            pass