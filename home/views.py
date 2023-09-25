from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from django.core.mail import send_mail

def index(request):
  subject='welcome to our software'
  message=f'thank you for login '
  email_from=settings.EMAIL_HOST_USER 
  recipient_list=['ishikasinghal2642005@gmail.com',]
  send_mail(subject,message,email_from,recipient_list)
  return HttpResponse('message sent')
    
  
  
# Create your views here.
