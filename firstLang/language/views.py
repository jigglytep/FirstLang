from django.http import HttpResponse
from django import forms
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from language.forms import HomeForm, QueryForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms.models import model_to_dict
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
from bs4 import BeautifulSoup

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def processReuquest(request, x):
    for i,num in enumerate(x):
        print(i,num)

    page = 'https://www.cybercoders.com/search/?searchterms=junior+developer&searchlocation=' + x[0]
    req =requests.get(page)
    soup = BeautifulSoup(req.text, 'html.parser')
    skill = soup.find_all("span",{"class":"skill-name"})

    return HttpResponse(x)


class SearchView(ListView):
    template_name= 'language/search.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
            d = request.POST.getlist('search')
            return processReuquest(request, d)
