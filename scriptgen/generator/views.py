import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Script
from .utils import handle_file_upload, generate_script_from_api
from django.http import HttpResponse


# View to handle script generation
@api_view(['POST'])
def generate_script(request):
    prompt = request.data.get('prompt')
    file = request.FILES.get('file')
    link = request.data.get('link')
    print(prompt)
    print(file)
    print(link)
    # Process the file and extract text
    extracted_text = handle_file_upload(file) if file else ''
    full_prompt = f"{prompt} {extracted_text}"

    # Call x.ai API to generate the script
    generated_script = generate_script_from_api(full_prompt, link)

    # Save the script in the database
    script = Script.objects.create(
        prompt=full_prompt,
        generated_script=generated_script
    )
    print(script)
    print("generated_script", generated_script)
    return JsonResponse({'generated_script': generated_script, 'script_id': script.id})


def home(request):
    return HttpResponse("Welcome to the AI Script Generator!")
