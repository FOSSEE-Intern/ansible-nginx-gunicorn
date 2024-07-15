from django.http import HttpResponse

def index(request):
    return HttpResponse("Test Page")

def about(request):
    return HttpResponse("Test About Page")
