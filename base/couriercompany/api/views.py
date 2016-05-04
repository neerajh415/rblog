from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from couriercompany.models import Couriercompany
from .serializers import CouriercompanySerializer, PostCreateSerializer, PreferencesSerializer
from rest_framework.decorators import api_view
import parser_utils
from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import copy
from django.shortcuts import render
from django.core import serializers
from rest_framework import generics
from couriercompany.api.permissions import IsOwner
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import permissions

class PostListApiView(ListAPIView):
	queryset = Couriercompany.objects.all()
	serializer_class = CouriercompanySerializer


class PostDetailAPIView(RetrieveAPIView):
	queryset = Couriercompany.objects.all()
	serializer_class = CouriercompanySerializer


class PostUpdateAPIView(UpdateAPIView):
	queryset = Couriercompany.objects.all()
	serializer_class = CouriercompanySerializer

class PostDeleteAPIView(DestroyAPIView):
	queryset = Couriercompany.objects.all()
	serializer_class = CouriercompanySerializer

class PostCreateAPIView(CreateAPIView):
	queryset = Couriercompany.objects.all()
	serializer_class = CouriercompanySerializer

#@api_view(['POST', 'GET'])
@csrf_exempt
def create_api(request):
	if request.method=='POST':
		post_qdict = copy.deepcopy(request.POST)
		form_details = parser_utils.qdict_to_dict(post_qdict)
		valid_pincode = Couriercompany.objects.filter(Q(pincode_id=form_details['pincode']) & Q(availability=True) & Q(limit__gt=form_details['limit']) or Q(limit='Notlimit'))
		data = {}
		for x in valid_pincode:
			data[int(x.__dict__['preference'])] = x.__dict__['courier']	
		return HttpResponse(json.dumps(data), content_type="application/json")
	else:
		data ={
   				"error": {
      				"message": "Unsupported get request. Please read the Graph API documentation at https://developers.facebook.com/docs/graph-api",
      						"type": "GraphMethodException",
      						"code": 100,
      							"pyck_id": "Ak7rd0w2yXV"
   						}
					}

		return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def home(request):
    return render(request, 'home.html')


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Couriercompany
    serializer_class = PostListApiView
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsOwner)