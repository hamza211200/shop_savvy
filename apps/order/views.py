from django.shortcuts import render
from django.http import JsonResponse
from .services import add_order,get_orders,get_order_items,get_order_by_id,get_order_item_by_id,update_item,update_order,delete_item,delete_order
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from utils.authUtils import jwt_required

# Create your views here.
@jwt_required
@require_http_methods(["GET"])
def get(request):
    return JsonResponse({"data":get_orders(request)})

@jwt_required
@require_http_methods(["GET"])
def get_id(request,order_id):
    return JsonResponse({"data":get_order_by_id(request,order_id)})

@jwt_required
@require_http_methods(["GET"])
def get_item(request,order_id):
    return JsonResponse({"data":get_order_items(request, order_id)})

@jwt_required
@require_http_methods(["GET"])
def get_order_id(request,order_id):
    return JsonResponse({"data":get_order_by_id(request,order_id)})

@jwt_required
@require_http_methods(["GET"])
def get_item_by_id(request,order_id,order_item_id):
    return JsonResponse({"data":get_order_item_by_id(request,order_id,order_item_id)})


@csrf_exempt
@jwt_required
@require_http_methods(["POST"])
def add(request):
    return JsonResponse({"data":add_order(request)})

@csrf_exempt
@jwt_required
@require_http_methods(["PUT"])
def update(request,order_id):
    return JsonResponse({"data" : update_order(request,order_id)})

@csrf_exempt
@jwt_required
@require_http_methods(["PUT"])
def update_items(request,order_item_id):
    return JsonResponse({"data" : update_item(request,order_item_id)})

@csrf_exempt
@jwt_required
@require_http_methods(["DELETE"])
def delete(request,order_id):
    return JsonResponse({"data" : delete_order(request,order_id)})


@csrf_exempt
@jwt_required
@require_http_methods(["DELETE"])
def delete_order_item(request,order_item_id):
    return JsonResponse({"data" : delete_item(request,order_item_id)})


