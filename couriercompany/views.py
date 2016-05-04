from django.shortcuts import render

# Create your views here.
@csrf_exempt
def home(request):
    return render(request, 'home.html')
