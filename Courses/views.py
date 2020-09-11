from django.shortcuts import render

from .models import *

# Create your views here.
def course(request):
	courses = Course.objects.all()
	context = {'courses':courses}
	return render(request, 'courses/courses.html', context)


        
