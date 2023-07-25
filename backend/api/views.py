from django.shortcuts import render
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.

"""def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    print(request.GET)
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    #print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)"""

"""def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        #data['id'] = model_data.id
        #data['title'] = model_data.title
        #data['content'] = model_data.content
        #data['price'] = model_data.price
        data = model_to_dict(model_data,)#fields=['id', 'title']
    return JsonResponse(data)"""

"""@api_view(['POST'])
def api_home(request, *args, **kwargs):
   
    #DRF API View 
    
    data = request.data
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #data = model_to_dict(instance, fields=['id', 'title', 'price'])
        data = ProductSerializer(instance).data
    return Response(data)"""

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View 
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        print(serializer.data)
        data = serializer.data
        return Response(data)