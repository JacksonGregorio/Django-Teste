from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import User
import json


def user_list(request):
    if request.method == "GET":
        users = list(User.objects.values())  
        return JsonResponse(users, safe=False)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def user_create(request):
    if request.method == "POST":
        data = json.loads(request.body)  
        user = User.objects.create(**data)  
        return JsonResponse({'id': user.pk}, status=201)  
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        data = json.loads(request.body)  
        for field, value in data.items():
            setattr(user, field, value) 
        user.save()
        return JsonResponse({'id': user.pk})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return JsonResponse({'id': pk})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

@csrf_exempt
def check_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "GET":
        user = User.objects.get(pk=pk)
        return JsonResponse({'id': user.pk, 'name': user.name, 'email': user.email, 'score': user.score, 'type': user.type})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
    
@csrf_exempt
def zero_score(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user = User.objects.get(pk=pk)
        user.score = 0
        user.save()
        return JsonResponse({'id': user.pk, 'score': user.score})
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
    
@csrf_exempt
def order_by_score(request):
    if request.method == "GET":
        users = list(User.objects.values().order_by('-score'))
        return JsonResponse(users, safe=False)
    return JsonResponse({'error': 'Invalid HTTP method'}, status=405)
    



