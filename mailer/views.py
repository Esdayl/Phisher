from django.core.mail import send_mail

def send_hook():
    send_mail(
        subject = 'Subject',
        message= 'Message Body',
        from_email = 'sender email',
        recipient_list = ['receiver emails'],
        fail_silently=False
    )

def send_feedback():
    send_mail(
        subject = 'Subject',
        message= 'Message Body',
        from_email = 'sender email',
        recipient_list = ['receiver emails'],
        fail_silently=False
    )