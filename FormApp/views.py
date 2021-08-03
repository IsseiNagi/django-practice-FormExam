from django.shortcuts import render
from . import forms
from .models import Students
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.


def setform(request):
    form = forms.StudentsModelForm()
    if request.method == 'POST':
        form = forms.StudentsModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'form.html', context={
        'form': form
    })


def students_list(request):
    students = Students.objects.all()
    return render(request, 'students_list.html', context={
        'students': students
    })


# idを受けて該当生徒を取り出し編集する
def update_student(request, id):
    student = Students.objects.get(id=id)
    update_form = forms.StudentsUpdateForm(
        initial={
            'name': student.name,
            'age': student.age,
            'grade': student.grade,
            'picture': student.picture,
        }  # 初期値の指定
    )
    # 取り出して編集して保存
    if request.method == 'POST':
        update_form = forms.StudentsUpdateForm(request.POST or None, request.FILES or None)
        if update_form.is_valid():
            student.name = update_form.cleaned_data['name']
            student.age = update_form.cleaned_data['age']
            student.grade = update_form.cleaned_data['grade']
            picture = update_form.cleaned_data['picture']
            if picture:
                fs = FileSystemStorage()
                file_name = fs.save(os.path.join('student', picture.name), picture)
                student.picture = file_name
            student.save()
    return render(
        request, 'update_student.html', context={
            'update_form': update_form,
            'student': student
        }
    )


# 既存生徒データの削除
def delete_student(request, id):
    delete_form = forms.StudentDeleteForm(
        initial={
            'id': id
        }
    )
    if request.method == 'POST':
        delete_form = forms.StudentDeleteForm(request.POST or None)
        if delete_form.is_valid():
            Students.objects.get(id=delete_form.cleaned_data['id']).delete()
    return render(
        request, 'delete_student.html', context={
            'delete_form': delete_form
        }
    )