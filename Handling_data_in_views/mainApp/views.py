from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import requests

@api_view(["GET"])
def products(request):
    data = product.objects.all()
    serializer = productSerializer(data,many=True)
    return Response({"Product":serializer.data})


def data_fetch(request):
    response = requests.get("http://127.0.0.1:8000/products")
    external_data = response.json()
    return render(request,"index.html",{"external_data":external_data})