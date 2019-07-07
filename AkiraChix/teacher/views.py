<<<<<<< HEAD
from django.shortcuts import render,redirect
=======
from django.shortcuts import render
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
from .forms import TeacherForm
from .models import Teacher

# Create your views here.

def add_teacher(request):
	form = TeacherForm()

	if request.method == 'POST':
		form = TeacherForm(request.POST)

		if form.is_valid(): #checks for errors
			form.save()

<<<<<<< HEAD
			return redirect('list_teachers')

=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
	else:
		forms = TeacherForm()

	return render(request, "add_teacher.html", {"form" : form})


def list_teachers(request):
	teachers = Teacher.objects.all()
	return render(request, "all_teachers.html", {"teachers" : teachers})
<<<<<<< HEAD


def teacher_details(request,pk):
	teacher = Teacher.objects.get(pk=pk)
	return render(request, "teacher_details.html", {"teacher":teacher})	


def edit_teacher(request,pk):
	teacher = Teacher.objects.get(pk=pk)

	if request.method == 'POST':
		form = TeacherForm(request.POST, instance = teacher)
		if form.is_valid():
			form.save()

			return redirect('list_teachers')


	else:
		form = TeacherForm(instance = teacher)

	return render(request, "edit_teacher.html", {"form":form})				
=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
