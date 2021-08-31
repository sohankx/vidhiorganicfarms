from .forms import SentForm
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def contact_form(request):
    if request.method == 'GET':
        contact_form = SentForm()
        context = {'contact_form': contact_form}
    else:
        contact_form =  SentForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            mail = contact_form.cleaned_data['email']
            sub = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']
            title = "Blogs"
            try:
                send_mail('Email from ' + str(mail),
                      "name: \n" + str(name) + "\n"
                        "email:\n" + str(mail) + "\n"
                        "subject: \n" + str(sub) + "\n"
                         "Title: "+str(title)+"\n\n"
                        "message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['sohanceh@gmail.com'],
                      # ['knarula@kineticxtech.com'],
                      )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            context = {
                'contact_form': contact_form,
                'name':name,
                'email':mail,
                'sub':sub,
                'message': message,
                'title':title

            }
    return context