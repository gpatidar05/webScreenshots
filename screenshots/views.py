from django.shortcuts import render
from screenshots.models import Website

def landing(request):
  response = {}
  response['websites'] = Website.objects.all()
  return render(request,'screenshots/landing.html',response)
