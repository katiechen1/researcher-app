from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Researcher 
from .models import NominateForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.core.mail import send_mail

def home(request):
    r = Researcher.objects.all()
    return render(request, 'home.html', {'researcher': r})

def researcher_detail(request, id):

    # return HttpResponse('<p> r detail view w id {} </p>'.format(id))
    try:
        r = Researcher.objects.get(id=id)
    except Researcher.DoesNotExist:
        raise Http404('Researcher not found')
    return render(request, 'researcher_detail.html', {'researcher': r})

def nominee_info(request):
    return


def nominate(request):
    form_class = NominateForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            nominee_name = request.POST.get('nominee_name', '')
            nominee_email = request.POST.get('nominee_email', '')
            nominee_website = request.POST.get('nominee_website', '')
            nominee_institution = request.POST.get('nominee_institution', '')
            form_content = request.POST.get('nominee_description', '')

            # Email the profile with the 
            # contact information
            template = get_template('nominate_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)


            #This emails us[katiechen@berkeley.edu] the submission from the form 
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['katiechen@berkeley.edu'],
                headers = {'Reply-To': contact_email }
            )
            email.send()

            #TODO: Email the candidate for confirmation 
            send_mail(
                'Nomination Confirmation for X_List',
                'Hello, you have been nominated for X_list. Please provide this in this format. Thanks',
                'katiechen@berkeley.edu',
                ['insert_email_here'],
                fail_silently=False,
            )

            return redirect('nominate')
    return render(request, 'nominate.html', {
        'form': form_class,
    })

