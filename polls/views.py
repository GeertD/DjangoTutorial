from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def goodbye(request):
    return HttpResponse("Goodbye stranger...")