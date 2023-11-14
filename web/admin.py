from os import name
from django.contrib import admin
from .models import Expense , Income , Token

# Register your models here.
class ExpenseAdmin (admin.ModelAdmin):
    list_display = ("text","user","date")

class IncomeAdmin(admin.ModelAdmin):
    list_display = ("text","user","date")
    
class TokenAdmin(admin.ModelAdmin):
    list_display = ("user","id")

admin.site.register(Expense , ExpenseAdmin)
admin.site.register(Income , IncomeAdmin)
admin.site.register(Token , TokenAdmin)