from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
def reg(request):
    template = loader.get_template('reg.html')
    context = {}
    return HttpResponse(template.render(context, request))

def rate(request):
    template = loader.get_template('rate.html')
    context = {}
    return HttpResponse(template.render(context, request))

def all(request):
    template = loader.get_template('all.html')
    context = {}
    return HttpResponse(template.render(context, request))