from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from chutiyaap.services.chutiyaap_services import add
class Avinash(APIView):


    def post(self,request,*args,**kwargs):
        data = request.data
        id = data['id']
        id1 = data['id1']
        print(id,id1)
        value = add(id,id1)
        return Response({'message':value},status=200)