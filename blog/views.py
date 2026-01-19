from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Create and save student
        student = Student.objects.create(
            name=name,
            email=email,
            age=int(number)
        )
        success = True
    
    return render(request, 'blog/index.html', {'success': success})
    