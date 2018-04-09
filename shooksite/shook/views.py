from django.shortcuts import render

from django.http import HttpResponse
from shook.models import Lead
from shook.serializers import LeadSerializer, UserSerializer
from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return Response(UserSerializer(request.user,
                context={'request':request}).data)
        return super(UserViewSet, self).retrieve(request, pk)