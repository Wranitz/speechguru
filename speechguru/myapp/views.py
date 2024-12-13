from django.shortcuts import render, HttpResponse
from .models import TodoItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request, "home.html")

def todos(request):
    items = TodoItem.objects.all
    return render(request, "todos.html",{"todos": items})

def sathi(request):
    return render(request, "sathi.html")

@csrf_exempt
def transcribe(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #Transcription logic here
            response_data = {'message': 'Transcription successful'}
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        retuen JsonResponse({'error': 'Invalid request method'}, status=405)