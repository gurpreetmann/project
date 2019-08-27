from django.shortcuts import render

# Create your views here.

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from trial.services.lets_multiply import multiply_value
class mult(APIView):


    def post(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        id1 = data['id1']
        print(id,id1)
        value = multiply_value(id,id1)
        return Response({'message':value},status=200)