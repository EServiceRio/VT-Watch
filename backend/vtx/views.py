from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import OsSerializer
from .models import OS

class OsList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = OS.objects.all()
    serializer_class = OsSerializer

class OsDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = OS.objects.all()
    serializer_class = OsSerializer
    
