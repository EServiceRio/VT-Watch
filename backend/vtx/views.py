from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import OsSerializer
from .serializer import GatewaySerializer, NodeSerializer, NodeSetupSerializer, HistSerializer, EventoSerializer
from .models import OS
from .models import Gateway, Node, NodeSetup, Hist, Evento

class OsList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = OS.objects.all()
    serializer_class = OsSerializer

class OsDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = OS.objects.all()
    serializer_class = OsSerializer

class GatewayList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

class GatewayDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

class NodeList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class NodeSetupList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = NodeSetup.objects.all()
    serializer_class = NodeSetupSerializer

class NodeSetupDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = NodeSetup.objects.all()
    serializer_class = NodeSetupSerializer

class HistList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Hist.objects.all()
    serializer_class = HistSerializer

class HistDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = Hist.objects.all()
    serializer_class = HistSerializer

class EventoList(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class EventoDetail(generics.RetrieveUpdateDestroyAPIView):    
    permission_classes=[IsAuthenticated]
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def DxmStatus(request):
    modelo = Gateway.objects.all()[0]
    data = {
        'online':modelo.online,
        'nome': modelo.name
    }
    return Response(data)