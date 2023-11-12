from os import name
from django.contrib import admin
from .models import Expense , Income

# Register your models here.
class ExpenseAdmin (admin.ModelAdmin):
    list_display = ("text","user","date")

class IncomeAdmin(admin.ModelAdmin):
    list_display = ("text","user","date")

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Income , IncomeAdmin)