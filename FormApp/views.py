from django.shortcuts import render
from . import forms

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
