from django.shortcuts import render

from application.forms import StudentForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def contact(request):
    form = StudentForm ()
    return render(request, 'contact.html', {'form': form})
