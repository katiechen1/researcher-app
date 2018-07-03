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
from .forms import UserForm 

# from .models import NewForm

# from .models import Nominee
# from .models import Nomination 

def home(request):
    r = Researcher.objects.all()
    return render(request, 'home.html', {'researcher': r})

def about(request):
    return render(request, 'about.html')

def thanks(request):
    return render(request, 'thanks.html')

def nomthanks(request):
    return render(request, 'nomthanks.html')

def badinfo(request):
    return render(request, 'badinfo.html')

def success(request):
    return render(request, 'success.html')

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
            
            nominators_name = request.POST.get('nominators_full_name', '')
            nominators_email = request.POST.get('nominators_email', '')
            nominees_name = request.POST.get('nominees_name', '')
            nominees_email = request.POST.get('nominees_email', '')
            
            d = { 'nominee_name': nominees_name, 'nominator': nominators_name }

            subject = 'Women in Microfluidics: Accept your nomination to our grassroots list'
            from_email = settings.EMAIL_HOST_USER
            to_email = [str(nominees_email)]
            text_content = render_to_string("temp1.txt", d)
            html_content = render_to_string("temp1.html", d)

            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect('/thanks')
        else:
            return redirect('/badinfo')
    return render(request, 'nominate.html', {
        'form': form_class,
    })

#prompts nominee to fill out information they want displayed
def nominee_info(request):
    form_class = NominatedInfo
    new_nominee = Researcher()

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():

            new_nominee.name = request.POST.get('name', '')
            ###
            new_nominee.email = request.POST.get('your_email', '')
            new_nominee.institution = request.POST.get('institution', '')
            new_nominee.position = request.POST.get('position', '')
            new_nominee.country = request.POST.get('country', '')
            new_nominee.website_link = request.POST.get('website', '')
            new_nominee.linkedin_link = request.POST.get('linkedin', '')
            new_nominee.level = request.POST.get('level', '')
            new_nominee.des = request.POST.get('description', '')
            new_nominee.save()
            return redirect('/success')
        else:
            return redirect('/badinfo')
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























