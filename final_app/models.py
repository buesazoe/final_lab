from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    profile_image = models.ImageField(upload_to='employee_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class LeaveRequest(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()

    def __str__(self):
        return f"Leave Request for {self.employee} ({self.start_date} to {self.end_date})"
    
class Attendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendance for {self.employee} on {self.check_in.date()}"

class Task(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return self.title
