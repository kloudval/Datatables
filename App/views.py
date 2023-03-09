from django.shortcuts import render
from .models import Employee


# Function to render homepage
def home(request):
    employee_list = Employee.objects.all()
    context = {
        'employees': employee_list,
    }
    return render(request, 'App/home.html', context)
