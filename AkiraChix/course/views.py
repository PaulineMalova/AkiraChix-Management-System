from django.shortcuts import render
from .forms import CourseForm
from .models import Course

# Create your views here.

def add_course(request):
	form = CourseForm()

	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()

	else:
		form = CourseForm()		
	return render(request, "add_course.html", {"form" : form})


def list_courses(request):
	courses = Course.objects.all()
	return render(request, "all_courses.html", {"courses" : courses})
