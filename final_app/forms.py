from django import forms
from .models import LeaveRequest, Attendance, Task

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'start_date', 'end_date', 'reason']

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("End date must be equal to or after the start date.")

        return cleaned_data

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'check_in', 'check_out']

    widgets = {
        'check_in': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'check_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']