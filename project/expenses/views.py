from django.shortcuts import render
from django.http import HttpResponse
from expenses.models import Summary, Detail

def index(request):
    total = Summary.objects.count()
    return HttpResponse(f"<h1><strong>Hello, world.</strong></h1><h3 style='color: red;'>You're at the expenses index.</h3><p>You have { total } summary records.</p>")