from django.shortcuts import render
from .models import detail
from .serializers import BoardSerializer, BoardDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from knox.auth import TokenAuthentication
from .permissions import IsOwnerOrReadOnly

# Create your views here.
# api쓰기
class detailAPI(generics.ListCreateAPIView):
    queryset = detail.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class detailDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = detail.objects.all()
    serializer_class = BoardDetailSerializer

