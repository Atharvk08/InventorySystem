from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView 

from .models import Product

class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        return Response(list(products))