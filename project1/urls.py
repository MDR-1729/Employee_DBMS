from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('<int:id>/',views.detail,name='employee_detail'),
    path('add/',views.add_employee),
    path('success/',views.success_view,name='employee_success')
]
