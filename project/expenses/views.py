from django.http import HttpResponse

def index(request):
  return HttpResponse("<h1><strong>Hello, world.</strong></h1><h3 style='color: red;'>You're at the expenses index.</h3>")