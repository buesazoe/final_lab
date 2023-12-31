from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .models import Department, Employee, LeaveRequest, Attendance, Task, LeaveRequest
from .forms import LeaveRequestForm, AttendanceForm, Task
from .forms import LeaveRequestForm, Attendance, TaskForm


class HomePageView(TemplateView):
    template_name = 'base.html'
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'

class LeaveRequestListView(ListView):
    model = LeaveRequest
    template_name = 'leave_request_list.html'
    context_object_name = 'leave_requests'
class LeaveRequestCreateView(CreateView):
    model = LeaveRequest
    form_class = LeaveRequestForm
    template_name = 'leave_request_create.html'
    success_url = '/leave-requests/'  # Redirect to the leave request list after successful form submission

def leave_request_create(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave-request-list')
    else:
        form = LeaveRequestForm()

    return render(request, 'leave_request_create.html', {'form': form})

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list.html'
    context_object_name = 'attendances'


def create_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance-list')
    else:
        form = AttendanceForm()

    return render(request, 'create_attendance.html', {'form': form})


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = '/task-list/'  # Redirect to the task list after successful form submission

# Add the following imports to the top of views.py
from django.http import HttpResponseRedirect
from django.urls import reverse

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('task-list'))
    else:
        form = TaskForm()

    return render(request, 'create_task.html', {'form': form})
