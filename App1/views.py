from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings
from .forms import SentForm
# Create your views here.

def sending_mail(request):
    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail('Email from '+str(mail),
                "name: \n"+str(name)+"\n"
                "email:\n"+str(mail)+"\n"
                "subject: \n"+str(sub)+"\n"
                "message :\n"+ str(message),
                settings.EMAIL_HOST_USER,
                ['apuri@kineticxtech.com'],
                # ['knarula@kineticxtech.com'],
                fail_silently=False )
            send_mail('Email from ' + str(mail),
                      "name: \n" + str(name) + "\n"
                        "email:\n" + str(mail) + "\n"
                        "subject: \n" + str(sub) + "\n"
                        "message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['sgandhi@kineticxtech.com'],
                      fail_silently=False)
            return HttpResponseRedirect('/App1/thanks/')
            # return render(request, 'thanks.html', {'success': '1'})
    else:
        form = SentForm()
    return render(request,'home.html',{'form': form})

def thanks(request):
    return render(request,'thanks.html')

# def contact_us(request):
#     return render(request,'contact_us.html')

