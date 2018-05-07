from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.template import RequestContext

from django.shortcuts import render_to_response,get_object_or_404
from django.shortcuts import render
from django.template import loader
# view function must return an HTTP response
def index(request):
  return HttpResponse("App successfully deployed")
