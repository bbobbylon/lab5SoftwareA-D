from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    hello = {"Message" : "Hello World!"}
    #return HttpResponse("Hello, world. You are in the Polls index.")
    return JsonResponse({'message' : hello})