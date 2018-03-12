from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Researcher 
from .models import NominateForm

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

def nominate(request):
    form_class = NominateForm
    return render(request, 'nominate.html', {
        'form': form_class,
    })

