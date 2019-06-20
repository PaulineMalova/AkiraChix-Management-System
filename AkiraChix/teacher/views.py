from django.shortcuts import render
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def add_teacher(request):
	form = TeacherForm()

	if request.method == 'POST':
		form = TeacherForm(request.POST)

		if form.is_valid(): #checks for errors
			form.save()

	else:
		forms = TeacherForm()

	return render(request, "add_teacher.html", {"form" : form})


def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request, "all_teachers.html", {"teachers" : teachers})
