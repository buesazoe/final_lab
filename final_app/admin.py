from django.contrib import admin
# admin.py

from django.contrib import admin
from .models import Department, Employee, LeaveRequest, Attendance, Task

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'age', 'salary', 'department', 'created_at', 'updated_at']

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['employee', 'start_date', 'end_date', 'reason', 'created_at', 'updated_at']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'check_in', 'check_out', 'created_at', 'updated_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'assigned_to', 'due_date', 'created_at', 'updated_at']
