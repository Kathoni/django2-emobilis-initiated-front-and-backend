from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Correct import for messages

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
            messages.success(request, 'Student record has been added successfully.')
            return redirect('contact')
    else:
        form = StudentForm()
    return render(request, 'contact.html', {'form': form})

def edit(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes have been saved.')
            return redirect('aboutus')
        else:
            messages.error(request, 'Something went wrong.')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html', {'form': form, 'student': student})

def delete(request, id):
    student = get_object_or_404(Student, id=id)

    try:
        student.delete()
        messages.success(request, 'Your changes have been deleted.')
    except Exception as e:
        messages.error(request, "Something went wrong.")

    return redirect('aboutus')