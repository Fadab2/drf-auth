from rest_framework import generics
from .serializer import SnackSerializer
from .models import Snack
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class SnackList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
