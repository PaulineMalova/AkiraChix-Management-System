from django.urls import path
<<<<<<< HEAD
from .views import add_student, list_students, student_details, edit_student
=======
from .views import add_student, list_students
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e

# from .views import profile_picture_view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('add/', add_student, name = 'add_student'),
<<<<<<< HEAD
	path('list/', list_students, name = 'list_students'),
	path('view/<int:pk>/', student_details, name='student_details'),
	path('edit/<int:pk>/', edit_student, name='edit_student'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

=======
	path('list/', list_students, name = 'list_students')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> 7c5cb535c33da0829c62f57c0c53b1da404afb7e

