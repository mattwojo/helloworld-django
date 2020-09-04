from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World! Django is running!")