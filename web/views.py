from datetime import datetime
from json import JSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from web.models import User,Token,Expense,Income


@csrf_exempt
def submit_expense(request):
    # user submits an expense
    
    #TODO : validate all
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Expense.objects.create(user = this_user , amount = request.POST['amount'],
                           text = request.POST['text'], date = date)
    
    return JsonResponse({
        'status': "ok",
    } , JSONEncoder)
    
    
@csrf_exempt
def submit_income(request):
    # user submits an expense
    
    #TODO : validate all
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    Income.objects.create(user = this_user , amount = request.POST['amount'],
                           text = request.POST['text'], date = date)
    
    return JsonResponse({
        'status': "ok",
    } , JSONEncoder)
