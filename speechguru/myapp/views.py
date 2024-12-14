from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html",{"todos": items})

def sathi(request):
    return render(request, "sathi.html")


def modelui(request):
    if request.method == 'POST':
        try:
            print(request)
            response_data = {'message': 'Prompt successful'}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': 'Invalid request method'}, status=405)
            return render(request, "modelui.html")
            
            
    return render(request, "modelui.html")

@csrf_exempt
def transcribe(request):
    if request.method == 'POST':
        try:
            audio_data = request.body
            #Transcription logic here 
            response_data = {'message': 'Transcription successful'}
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': 'Invalid request method'}, status=405)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)