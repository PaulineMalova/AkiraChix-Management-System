from django.urls import path
<<<<<<< HEAD
from .views import add_teacher, list_teachers, teacher_details, edit_teacher
=======
from .views import add_teacher, list_teachers
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e

urlpatterns = [
	path('add/', add_teacher, name = 'add_teacher'),
	path('list/', list_teachers, name= 'list_teachers'),
<<<<<<< HEAD
	path('view/<int:pk>/', teacher_details, name = 'teacher_details'),
	path('edit/<int:pk>/', edit_teacher, name = 'edit_teacher'),
=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
]