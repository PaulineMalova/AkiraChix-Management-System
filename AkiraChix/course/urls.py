from django.urls import path
<<<<<<< HEAD
from .views import add_course, list_courses, course_details, edit_course
=======
from .views import add_course, list_courses
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e

urlpatterns = [
	path('add/', add_course, name = 'add_course'),
	path('list/', list_courses, name = "list_courses"),
<<<<<<< HEAD
	path('view/<int:pk>/', course_details, name = "course_details"),
	path('edit/<int:pk>/', edit_course, name = "edit_course"),
=======
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e
]