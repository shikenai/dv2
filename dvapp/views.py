from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return JsonResponse({"users": {
        {"id": "1", "name": "taro"},
        {"id": "2", "name": "jiro"},
    }})
