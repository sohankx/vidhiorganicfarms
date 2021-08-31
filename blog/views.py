from django.views import generic
from django.contrib import messages
from .models import Post,Gallery
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from . import forms
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from .forms import SentForm,Subscribe
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def home(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        form = SentForm(request.POST)
        form1 = Subscribe(request.POST)
        if form.is_valid():
            name= form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            title = "Home page"
            send_mail('Email from '+str(mail),
                "Name: "+str(name)+"\n\n"
                "Email: "+str(mail)+"\n\n"
                "Subject: "+str(sub)+"\n\n"
                "Title: "+str(title)+"\n\n"
                "Message :\n"+ str(message),
                settings.EMAIL_HOST_USER,
                # ['ritik411@gmail.com'],
                ['apuri@kineticxtech.com'],
                fail_silently=False )
            send_mail('Email from ' + str(mail),
                      "Name: " + str(name) + "\n"
                        "Email: " + str(mail) + "\n"
                        "Subject: " + str(sub) + "\n"
                                                 "Title: "+str(title)+"\n\n"
                        "Message :" + str(message),

                      settings.EMAIL_HOST_USER,
                      ['sgandhi@kineticxtech.com'],
                      fail_silently=False)
            # return HttpResponseRedirect('/App1/thanks/')
            # return render(request, 'thanks.html')
            messages.success(
                request, 'Thank you for getting in touch. We got your request and within 2 business days, we will get in touch.')
        elif form1.is_valid():
            sub = forms.Subscribe(request.POST)

            subject = 'Welcome to KineticXTech'
            message = 'You have Subscribed on KineticxTech'
            recepient = str(sub['Email'].value())
            send_mail(subject,
                      message, settings.EMAIL_HOST_USER, [recepient, 'apuri@kineticxtech.com'], fail_silently=False)
            # return render(request, 'thanks.html')
            messages.success(
                request, 'Thank You For Subscribing Us!')
    else:
        form = SentForm()
        form1 = Subscribe()
    return render(request,'index.html',{'form': form,'form1': form1})
    # return render(request,'index.html')
#
def blog_grid_sidebar(request):
    return render(request,'blog_grid_sidebar.html')

def accounts(request):
    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            title = "Accounts page"
            send_mail('Email from ' + str(mail),
                      "Name: " + str(name) + "\n\n"
                     "Email: " + str(mail) + "\n\n"
                      "Subject: " + str(sub) + "\n\n"
                                               "Title: "+str(title)+"\n\n"
                       "Message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['apuri@kineticxtech.com'],
                      # ['knarula@kineticxtech.com'],
                      fail_silently=False)
            send_mail('Email from ' + str(mail),
                      "Name: " + str(name) + "\n\n"
                      "Email: " + str(mail) + "\n\n"
                      "Subject: " + str(sub) + "\n\n"
                                               "Title: "+str(title)+"\n\n"
                      "Message :" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['sgandhi@kineticxtech.com'],
                      fail_silently=False)
            # return HttpResponseRedirect('/App1/thanks/')
            return render(request, 'thanks.html')
    else:
        form = SentForm()
    return render(request, 'accounts.html', {'form': form})
    # return render(request,'index.html')
#
#
# def assets(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "Assets page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'assets.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def procurement(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "Procurement page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'procurement.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def production(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "production page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'production.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
def page_about_us(request):
    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['email']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            title = "About Us page"
            send_mail('Email from ' + str(mail),
                      "name: \n" + str(name) + "\n"
                        "email:\n" + str(mail) + "\n"
                        "subject: \n" + str(sub) + "\n"
                                                   "Title: "+str(title)+"\n\n"
                        "message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['apuri@kineticxtech.com'],
                      # ['knarula@kineticxtech.com'],
                      fail_silently=False)
            send_mail('Email from ' + str(mail),
                      "name: \n" + str(name) + "\n"
                      "email:\n" + str(mail) + "\n"
                      "subject: \n" + str(sub) + "\n"
                                                 "Title: "+str(title)+"\n\n"
                      "message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                  ['sgandhi@kineticxtech.com'],
                      fail_silently=False)
            # return HttpResponseRedirect('/App1/thanks/')
            return render(request, 'thanks.html')
    else:
        form = SentForm()
    return render(request, 'page_about_us.html', {'form': form})
    # return render(request,'index.html')
    # return render(request,'page_about_us.html')
#
#
def page_contact(request):
    if request.method == 'POST':
        form = SentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            sub = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            title = "About Us page"
            send_mail('Email from ' + str(mail),
                      "name: \n" + str(name) + "\n"
                        "email:\n" + str(mail) + "\n"
                        "phone:\n" + str(phone) + "\n"
                        "subject: \n" + str(sub) + "\n"
                                                   "Title: "+str(title)+"\n\n"
                        "message :\n" + str(message),
                      settings.EMAIL_HOST_USER,
                      ['ankitrania5@gmail.com'],
                      # ['knarula@kineticxtech.com'],
                      fail_silently=False)
            # send_mail('Email from ' + str(mail),
            #           "name: \n" + str(name) + "\n"
            #           "email:\n" + str(mail) + "\n"
            #           "subject: \n" + str(sub) + "\n"
            #                                      "Title: "+str(title)+"\n\n"
            #           "message :\n" + str(message),
            #           settings.EMAIL_HOST_USER,
            #       ['sgandhi@kineticxtech.com'],
            #           fail_silently=False)
            # return HttpResponseRedirect('/App1/thanks/')
            return render(request, 'thanks.html')
    else:
        form = SentForm()
    return render(request,'page_contact.html', {'form': form})

# @csrf_exempt
# def contact_lead(request):
#     if request.method=='POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         company = request.POST['company']
#         address = request.POST['address']
#         message = request.POST['message']
#         url2 = 'https://office.kxterp.com/api/resource/Lead/'
#         data2 = {"lead_name": name, "email_id": email, "phone": phone,"status":"Lead","source":"Website","company_name": company,"address":address,"message": message,"api": 1}
#         data2 = json.dumps(data2)
#         res2 = requests.post(url=url2, verify=False, data=data2)
#         # print(res2.text)
#
#
#     return render(request,'page_contact.html', {'success': '1'})
# #
#
# def page_careers(request):
#     return render(request,'page_careers.html')
#
def products(request):
    return render(request,'products.html')
#
# def Cookie_Policy(request):
#     return render(request,'gallery.html')
#
# def Terms_Conditions(request):
#     return render(request,'Terms&Conditions.html')
#
# def support(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "support page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'support.html', {'form': form})
#     # return render(request,'index.html')
#

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request,"gallery.html",{'gallery':gallery})


#
# def CRM(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "CRM page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'CRM.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def pms(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "PMS page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'pms.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def selling(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "selling page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'selling.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def HRMS(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "HRMS page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'HRMS.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def coming_soon(request):
#     return render(request,'coming_soon.html')
#
# def manufacturing(request):
#     return render(request,'manufacturing.html')
#
# def stock_inventory(request):
#     if request.method == 'POST':
#         form = SentForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             mail = form.cleaned_data['email']
#             sub = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             title = "Stock Inventory page"
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n\n"
#                                              "Email: " + str(mail) + "\n\n"
#                                                                      "Subject: " + str(sub) + "\n\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :\n" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['apuri@kineticxtech.com'],
#                       # ['knarula@kineticxtech.com'],
#                       fail_silently=False)
#             send_mail('Email from ' + str(mail),
#                       "Name: " + str(name) + "\n"
#                                              "Email: " + str(mail) + "\n"
#                                                                      "Subject: " + str(sub) + "\n"
#                                                                                               "Title: "+str(title)+"\n\n"
#                                                                                               "Message :" + str(
#                           message),
#                       settings.EMAIL_HOST_USER,
#                       ['sgandhi@kineticxtech.com'],
#                       fail_silently=False)
#             # return HttpResponseRedirect('/App1/thanks/')
#             return render(request, 'thanks.html')
#     else:
#         form = SentForm()
#     return render(request, 'stock_inventory.html', {'form': form})
#     # return render(request,'index.html')
#
#
#
# def clients(request):
#     return render(request,'clients.html')
#
# def policy(request):
#     return render(request,'policy.html')
#
# def consulting(request):
#     return render(request,'consulting.html')
#
class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog_grid_sidebar.html'
    paginate_by = 6

from django.shortcuts import get_list_or_404, get_object_or_404

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def post(self, request, slug):
      instance = get_object_or_404(Post, slug = slug)
      if request.method == 'POST':
          form = SentForm(request.POST)
          if form.is_valid():
              name = form.cleaned_data['name']
              mail = form.cleaned_data['email']
              sub = form.cleaned_data['subject']
              message = form.cleaned_data['message']
              title = "About Us page"
              send_mail('Email from ' + str(mail),
                        "name: \n" + str(name) + "\n"
                          "email:\n" + str(mail) + "\n"
                          "subject: \n" + str(sub) + "\n"
                                                     "Title: "+str(title)+"\n\n"
                          "message :\n" + str(message),
                        settings.EMAIL_HOST_USER,
                        ['apuri@kineticxtech.com'],
                        # ['knarula@kineticxtech.com'],
                        fail_silently=False)
              send_mail('Email from ' + str(mail),
                        "name: \n" + str(name) + "\n"
                        "email:\n" + str(mail) + "\n"
                        "subject: \n" + str(sub) + "\n"
                                                   "Title: "+str(title)+"\n\n"
                        "message :\n" + str(message),
                        settings.EMAIL_HOST_USER,
                    ['sgandhi@kineticxtech.com'],
                        fail_silently=False)
              # return HttpResponseRedirect('/App1/thanks/')
              messages.success(request, 'Form submission successful')
              return HttpResponseRedirect(instance.get_absolute_url())
      else:
          form = SentForm()
      return render(request, 'post_detail.html', {'form': form} )


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def edit_post(request, post_id=None):
    item = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'post_form.html', {'form': form})
