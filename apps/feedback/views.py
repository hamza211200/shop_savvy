from django.shortcuts import render
from . import services
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from utils.authUtils import jwt_required

# Create your views here.
@require_http_methods(["GET"])
def get(request):
    return JsonResponse({"message" : services.get_feedback(request)})

@require_http_methods(["GET"])
def get_by_id(request,user_id):
    return JsonResponse({"message":services.get_feedback_by_id(request,user_id)})


@csrf_exempt
@jwt_required
@require_http_methods(["POST"])
def add(request):
    return JsonResponse({"message" : services.add_feedback(request) })