import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import anthropic
import json
import requests


# Create your views here.
def test_view(request):
    return JsonResponse({'message': 'Hello, world!'})


@csrf_exempt
def ask_view(request):

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    client = anthropic.Anthropic(api_key=api_key)

    if request.method == 'POST':
        data = json.loads(request.body)
        phrase = data.get('phrase')
        if phrase:

            content = phrase

            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                temperature=0.1,
                system="You are a professional lawyer, you specialize in drafting contracts and agreements for my company and my clients. My company's name is  Bixmerchant and we are software development company. Always respond with HTML code",
                messages=[
                    {"role": "user", "content": content}
                ]
            )

            return JsonResponse({'response': message.content[0].text})
        else:
            return JsonResponse({'error': 'No phrase provided'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)