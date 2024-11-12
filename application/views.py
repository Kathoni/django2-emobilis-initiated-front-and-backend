from django.shortcuts import render, redirect
from application.forms import StudentForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = StudentForm()
    return render(request, 'contact.html', {'form': form})
