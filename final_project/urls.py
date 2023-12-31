from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from final_app.views import HomePageView, DepartmentListView, EmployeeListView, EmployeeDetailView, LeaveRequestListView, AttendanceListView, TaskListView, leave_request_create, create_attendance, create_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('leave-requests/', LeaveRequestListView.as_view(), name='leave-request-list'),
    path('leave-requests/create/', leave_request_create, name='leave-request-create'),
    path('attendances/', AttendanceListView.as_view(), name='attendance-list'),
     path('create-attendance/', create_attendance, name='create-attendance'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('create-task/', create_task, name='create-task')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
