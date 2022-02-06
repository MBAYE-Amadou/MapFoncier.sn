from django.shortcuts import render
from django.views.generic import TemplateView

# My view
class HomePageView(TemplateView):
	template_name = 'webmap.html'