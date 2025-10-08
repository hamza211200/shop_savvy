from django.shortcuts import render
from django.http import JsonResponse
from .services import get_product,get_product_id,add_product,update_product,delete_product
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@ require_http_methods(["GET"])
def get(request):
    return JsonResponse({"data": get_product(request) })

@require_http_methods(["GET"])
def get_id(request,product_id):
    return JsonResponse({"data" :get_product_id(request,product_id)})

@csrf_exempt
@require_http_methods(["POST"])
def add(request):
    return JsonResponse({"data":add_product(request)})

@csrf_exempt
@require_http_methods(["PUT"])
def update(request,product_id):
    return JsonResponse({"data" : update_product(request,product_id)})

@csrf_exempt
@require_http_methods(["DELETE"])
def delete(request,product_id):
    return JsonResponse({"data":delete_product(request,product_id)})