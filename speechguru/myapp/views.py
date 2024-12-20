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
            select_option = request.POST['select_option']
            prompt = request.POST['text_input']
            response_data = {'message': 'Prompt successful'}
            print(JsonResponse(response_data))
            return JsonResponse(response_data)
          
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
    



    # sadm
    #                document.getElementById('recordButton').disabled = true;
    #            document.getElementById('stopButton').disabled = false;
    #       } catch (error) {
    #           console.error('Error accessing the audio stream:', error);
    #           alert('There was an error accessing the audio stream.')
    #        }
    #    });
    #    document.getElementById('stopButton').addEventListener('click', () => {
    #        mediaRecorder.stop();
    #        document.getElementById('recordButton').disabled = false;
    #        document.getElementById('stopButton').disabled = true;
    #    });
    #</script>