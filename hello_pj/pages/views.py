from django.http import HttpResponse

# Create your views here.


def home_page_view(request):
    """Home page"""
    return HttpResponse("Hello world")
