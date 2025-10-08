from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .services import get_user,get_user_id, add_user, login_user,update_user,change_user_password
from utils.authUtils import jwt_required

# Create your views here.
@jwt_required
@require_http_methods(["GET"])
def get(request):
    return JsonResponse({"data": get_user(request)})

@jwt_required
@require_http_methods(["GET"])
def get_id(request,user_id):
    return JsonResponse({"data": get_user_id(request,user_id)})

@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    return JsonResponse({"data": add_user(request)})

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    return JsonResponse({"data": login_user(request)})


@jwt_required
@csrf_exempt
@require_http_methods(["PUT"])
def  update(request):
    return JsonResponse({"data":update_user(request)})

@jwt_required
@csrf_exempt
@require_http_methods(["PUT"])
def  change_password(request):
    return JsonResponse({"message":change_user_password(request)})

