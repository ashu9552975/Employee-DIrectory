
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home_page, name='home_page'),
    path('', views.admin_login, name='admin_login'),
    path('administrator/login', views.employee_list, name='employee_list'),
    path('employee/<int:pk>', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/login/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('employee/login', views.employee_login, name='employee_login'),
    # path('employee/login/<int:pk>/', views.employee_update, name='employee_update'),
    # path('employee/login', views.employee_update, name='employee_update'),
    
]
