from .models import Board
from .serializers import BoardSerializer, BoardDetailSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from knox.auth import TokenAuthentication
from .permissions import IsOwnerOrReadOnly


class BoardAPI(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # 로그인관련
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class BoardDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer
    # 로그인관련
    authentication_classes = [TokenAuthentication] # 토큰 
    permission_classes = [IsOwnerOrReadOnly]
