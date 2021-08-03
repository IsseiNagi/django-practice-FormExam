from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('form', views.setform, name='form'),
    path('students_list', views.students_list, name='students_list'),
    path('update_student/<int:id>', views.update_student, name='update_student'),
    path('delete_student/<int:id>', views.delete_student, name='delete_student'),
]
