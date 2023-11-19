from django.urls import path
from . import views

urlpatterns = [
    path('submit/expense/', views.submit_expense,name='submit_expense'),
    path('submit/income/', views.submit_income,name='submit_income'),
    path('accounts/register/', views.register,name='register'),
    path('', views.index, name='index'),
    path('edit/expense/',views.edit_expense, name='edit_expense'),
    path('edit/income/',views.edit_income, name ='edit_income'),
    path('q/incomes/',views.query_incomes, name='query_incomes'),
    path('q/expenses/',views.query_expenses, name='query_expenses'),
    path('accounts/whoami/', views.whoami, name='whoami'),
    path('accounts/login/',views.login, name='login'),
    path('news/', views.news, name='news'),
    path('accounts/logout/',views.logout, name='logout'),
]