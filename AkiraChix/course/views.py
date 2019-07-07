<<<<<<< HEAD
from django.shortcuts import render, redirect
=======
from django.shortcuts import render
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
from .forms import CourseForm
from .models import Course

# Create your views here.

def add_course(request):
	form = CourseForm()

	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()

<<<<<<< HEAD
			return redirect('list_courses')

=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
	else:
		form = CourseForm()		
	return render(request, "add_course.html", {"form" : form})


def list_courses(request):
	courses = Course.objects.all()
	return render(request, "all_courses.html", {"courses" : courses})
<<<<<<< HEAD


def course_details(request,pk):
	course = Course.objects.get(pk=pk)
	return render(request, "course_details.html", {"course":course})


def edit_course(request,pk):
	course = Course.objects.get(pk=pk)	

	if request.method == 'POST':
		form = CourseForm(request.POST, instance=course)
		if form.is_valid():
			form.save()

			return redirect('list_courses')

	else:
		form = CourseForm(instance = course)

	return render(request, "edit_course.html", {"form":form})		
=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
