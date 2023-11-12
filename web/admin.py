from os import name
from django.contrib import admin
from .models import Expense

# Register your models here.
class ExpenseAdmin (admin.ModelAdmin):
    list_display = ("text","user","date")

admin.site.register(Expense, ExpenseAdmin)