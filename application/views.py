from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Correct import for messages
from rest_framework import status
from rest_framework.decorators import api_view

from application.forms import StudentForm
from application.models import Student
from application.serializers import StudentSerializer


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

@api_view(['GET', 'POST'])     # Use a list to specify HTTP methods
def studentsapi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     # Corrected `serializer.errorsc` typo
