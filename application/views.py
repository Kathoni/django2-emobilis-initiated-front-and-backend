from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages

from application.forms import StudentForm
from application.models import Student


# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    data = Student.objects.all()

    return render(request, 'aboutus.html', {'data': data})

def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = StudentForm()
    return render(request, 'contact.html', {'form': form})

def edit(request, id):
    student = get_object_or_404(Student , id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form, 'student': student})