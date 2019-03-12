from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings

from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context

from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives

from .models import Researcher 
from .models import NominateForm
from .models import NominatedInfo
from .models import FeedbackForm
from .forms import UserForm 

import urllib.request
import json
# from .models import NewForm

# from .models import Nominee
# from .models import Nomination 

def home(request):
    r = Researcher.objects.all()
    return render(request, 'home.html', {'researcher': r})

def about(request):
    return render(request, 'about.html')

def feedback_thanks(request):
    return render(request, 'feedback_thanks.html')

def thanks(request):
    return render(request, 'thanks.html')

def nomthanks(request):
    return render(request, 'nomthanks.html')

def badinfo(request):
 
    return render(request, 'badinfo.html')

def nombadinfo(request):
    return render(request, 'nombadinfo.html')


def link_check(link):
    original = link
    if link == "":
        return ""
    http = link.find("http://")
    https = link.find("https://")
    if (http == -1 and https == -1):
        link = "http://" + link
    http = link.find("http://")
    https = link.find("https://")
    return link

def researcher_detail(request, id):

    try:
        r = Researcher.objects.get(id=id)
    except Researcher.DoesNotExist:
        raise Http404('Researcher not found')
    return render(request, 'researcher_detail.html', {'researcher': r})
    # try:
    #     r = Nominee.objects.get(id=id)
    # except Nominee.DoesNotExist:
    #     raise Http404('Researcher not found.')
    # return render(request, 'researcher_detail.html', {'researcher': r})


def nominate(request):
    form_class = NominateForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''
            if not result['success']:
                return redirect('/badinfo')

            nominators_name = request.POST.get('nominators_full_name', '')
            nominators_email = request.POST.get('nominators_email', '')
            nominees_name = request.POST.get('nominees_name', '')
            nominees_email = request.POST.get('nominees_email', '')
            # nominees_website = request.POST.get('nominees_website', '')
            # nominees_institution = request.POST.get('nominees_institution', '')

            # plaintext = get_template("temp1.txt")
            # html_temp = get_template("temp1.html")
            d = { 'nominee_name': nominees_name, 'nominator': nominators_name }

            subject = 'Women in Microfluidics: Accept your nomination to our grassroots list'
            from_email = settings.EMAIL_HOST_USER
            to_email = [str(nominees_email)]
            text_content = render_to_string("temp1.txt", d)
            html_content = render_to_string("temp1.html", d)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.send()

            d2 = {'nominator': nominators_name,'nominee_name': nominees_name}

            subject2 = 'Women in Microfluidics: Thank you for your nomination'
            from_email2 = settings.EMAIL_HOST_USER
            to_email2 = [str(nominators_email)]
            text_content2 = render_to_string("temp2.txt", d2)
            html_content2 = render_to_string("temp2.html", d2)

            msg2 = EmailMultiAlternatives(subject2, text_content2, from_email2, [to_email2])
            msg2.send()


            return redirect('/thanks')
        else:
            return redirect('/badinfo')
    return render(request, 'nominate.html', {
        'form': form_class,
    })

def feedback(request):
    form_class = FeedbackForm
    if request.method == 'POST':
        form = form_class(data = request.POST)
        if form.is_valid():
            feedback = request.POST.get('feedback_text', '')
            
            #send email
            subject = 'Feedback Form Submission'
            from_email = settings.EMAIL_HOST_USER
            to_email = [settings.EMAIL_HOST_USER]
            send_mail(subject,feedback,from_email,to_email,fail_silently=False,)

            return redirect('/feedback_thanks')
        else:
            return redirect('/badinfo')
    return render(request, 'feedback.html', {
                'form': form_class,
                    })

#prompts nominee to fill out information they want displayed
def nominee_info(request):
    form_class = NominatedInfo
    new_nominee = Researcher()

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,'response': recaptcha_response}
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if not result['success']:
                return redirect('/badinfo')



            new_firstname = request.POST.get('firstname', 'n/a')
            new_lastname = request.POST.get('lastname','n/a')
            new_fullname = new_lastname + ", " + new_firstname
            new_email = request.POST.get('email', 'n/a')
            new_institution = request.POST.get('institution', 'n/a')
            new_position = request.POST.get('position', 'n/a')
            new_country = request.POST.get('country', 'n/a')
            new_website_link = link_check(request.POST.get('website', 'n/a'))
            new_level = request.POST.get('level', 'n/a')
            new_des = request.POST.get('description', 'n/a')
            
            existing_nominees = Researcher.objects.filter(email = new_email).exclude(email = 'n/a')
            if len(existing_nominees) == 1:
                existing_nominee = existing_nominees[0]
                existing_nominee.firstname = new_firstname
                existing_nominee.lastname = new_lastname
                existing_nominee.fullname = new_fullname
                existing_nominee.email = new_email
                existing_nominee.institution = new_institution
                existing_nominee.position = new_position
                existing_nominee.country = new_country
                existing_nominee.website_link = new_website_link
                existing_nominee.level = new_level
                existing_nominee.des = new_des
                existing_nominee.save()
            elif len(existing_nominees) == 0:
                new_nominee.firstname = new_firstname
                new_nominee.lastname = new_lastname
                new_nominee.fullname = new_fullname
                new_nominee.email = new_email
                new_nominee.institution = new_institution
                new_nominee.position = new_position
                new_nominee.country = new_country
                new_nominee.website_link = new_website_link
                new_nominee.level = new_level
                new_nominee.des = new_des
                new_nominee.save()
            else:
                #handle multiple objects, but this shouldn't happen
                print("Multiple found, there's an issue")
                return redirect('/badinfo')
            return redirect('/nomthanks')
        # else:
        #     return redirect('/nombadinfo')
    return render(request, 'nomineeinfo.html', {
        'form': form_class,
    })


# # #creates new authenticated user 
# def register_user(request):
#     form_class = UserForm
#     template_name = 'nomineeinfo.html'
#     # new_nomination = Nomination

#     #creating a User 
#     if request.method == 'POST':
#         form = form_class(data=request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
    
#             user.set_password(password)
#             user.save()

#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 #user authenticated here, create new nomination object
#                 if user.is_active:
#                     login(request, user)

#                     #this should show the form for nominee to fill out
#                     return redirect('/thanks')
#         else:
#             return render(request, 'register.html', {
#         'form': form_class, })
#         return redirect('/')

#     #display empty form
#     elif request.method == 'GET':
#         return render(request, 'register.html', {
#         'form': form_class, })
#     return redirect('/')























