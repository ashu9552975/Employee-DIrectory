
from django.shortcuts import render, get_object_or_404, redirect
from .models import Member,Admin
from .forms import EmployeeForm
from django.contrib.auth.models import User
from django.http import HttpResponse



def home_page(request): return render(request, 'home_page.html')

def admin_login(request):
  if request.method == 'POST':
    print(request.POST)
    user = Admin.objects.get(email=request.POST['email'])
    print(user)
    if user:
      if user.password==request.POST['password']:
        return redirect (employee_list)
      else:
        return HttpResponse("wrong pass")
    else:
      return HttpResponse("user not found")
  else:
    return render(request, 'admin_login.html')


def employee_login(request):
  if request.method == 'POST':
    user = Member.objects.get(email=request.POST['email'])
    if user.password==request.POST['password']:
      return render(request, 'details.html', {'mymember': user})
    else:
      return HttpResponse("wrong pass")
  else:
    return render(request, 'login.html')


def employee_list(request):
    employees = Member.objects.all()
    print(employees)
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    return render(request, 'details.html', {'mymember': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})
