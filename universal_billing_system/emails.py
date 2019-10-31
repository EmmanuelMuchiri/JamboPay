from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.core.mail import send_mail
def send_notification(name,email,amount,quantity):
    # Creating message subject and sender
    subject = 'Pay bill'
    sender = 'emmahg6@gmail.com'

    text_content = render_to_string('email/bill.txt',{ "name": name,"amount":amount,"quantity":quantity })
    html_content = render_to_string('email/bill.html',{ "name": name,"amount":amount,"quantity":quantity })

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def send_message(name, receiver):
    subject = 'account created'
    sender = 'emmahg6@gmail.com'

    text_content = render_to_string('email/bill.txt',{ "name": name })
    html_content = render_to_string('email/bill.html',{ "name": name })

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

def welcome_email(name,receiver, password):
    subject ='Welcome to the Universal Billing System'
    sender = 'emmahg6@gmail.com'

    text_content = render_to_string('email/notify.txt',{"name": name, "password":password})
    html_content = render_to_string('email/notify.html',{"name":name, "password":password})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()