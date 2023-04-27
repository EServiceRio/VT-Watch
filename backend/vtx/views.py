from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import OsSerializer
from .serializer import GatewaySerializer, NodeSerializer, NodeSetupSerializer, HistSerializer, EventoSerializer
from django.shortcuts import HttpResponse
from django.views.generic import View
from django.db.models import Q
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import OS
from .models import Gateway, Node, NodeSetup, Hist, Evento

from .cicloLeitura import *

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


@method_decorator(csrf_exempt, name='dispatch')
class Filtra(View):
    def post(self,request):        
        try:
            user = str(request.POST['token'])
            token = Token.objects.filter(key=user).first()
            if not token:
                return HttpResponse('{"falha":"token inexistente"}')
        except Token.DoesNotExist:
            return HttpResponse('{"falha":"token inexistente"}')
        inis = str(request.POST['ini'])
        fims = str(request.POST['fim'])
        node = int(request.POST['node'])
        print(f'{inis}')
        print(f'{fims}')
        if inis == '':
            agora = datetime.now()
            inis = f'{agora.year}-{agora.month}-{agora.day}T0:0:0'
            fims = f'{agora.year}-{agora.month}-{agora.day}T23:59:0'
        iniDA=inis.split('T')[0].split('-')
        iniTA=inis.split('T')[1].split(':')
        fimDA=fims.split('T')[0].split('-')
        fimTA=fims.split('T')[1].split(':')
        ini = datetime(int(iniDA[0]),int(iniDA[1]),int(iniDA[2]),int(iniTA[0]),int(iniTA[1]),0)
        fim = datetime(int(fimDA[0]),int(fimDA[1]),int(fimDA[2]),int(fimTA[0]),int(fimTA[1]),0)
        ini += timedelta(hours=3)
        fim += timedelta(hours=3)
        print(f'{ini}')
        print(f'{fim}')
        dadof = Hist.objects.filter(Q(date__gt=ini) & Q(date__lt=fim) & Q(node=node)).order_by('date')
        strinfy = ""
        
        for hf in dadof:
            hora = int(hf.date.hour)-3
            if hora<0:
                hora+=23  
            hf.date = f'{hora}:{hf.date.minute} {hf.date.day}/{hf.date.month}/{hf.date.year}'
            #strinfy = f'{strinfy}{{"hora":"{hf.date}","X Veloc":{hf.vibraX/1000},"Z Veloc":{hf.vibraZ/1000},"X Acele":{hf.vibraX2/1000},"Z Acele":{hf.vibraZ2/1000},"Temperatura":{hf.temp/20},"Aler X Veloc":{hf.alertVibraX},"Aler Z Veloc":{hf.alertVibraZ},"Aler X Acele":{hf.alertVibraX2},"Aler Z Acele":{hf.alertVibraZ2},"Aler Temper":{hf.alertTemp}}},'
            strinfy = f'{strinfy}{{"hora":"{hf.date}","X Veloc":{hf.vibraX/1000},"Z Veloc":{hf.vibraZ/1000},"Temperatura":{hf.temp/20},"Corrente":{hf.corrente/100},"Aler X Veloc":{hf.alertVibraX},"Aler Z Veloc":{hf.alertVibraZ},"Aler Corrente":{hf.alertCorrente},"Aler Temper":{hf.alertTemp}}},'
        strinfy = "[" + strinfy[:len(strinfy)-1] + "]"
        return HttpResponse(strinfy)
        
@method_decorator(csrf_exempt, name='dispatch')
class Eventos(View):
    def post(self,request):
        inis = str(request.POST['ini'])
        fims = str(request.POST['fim'])
        print(f'{inis}')
        print(f'{fims}')
        if inis == '':
            agora = datetime.now()
            inis = f'{agora.year}-{agora.month}-{agora.day}T0:0:0'
            fims = f'{agora.year}-{agora.month}-{agora.day}T23:59:0'
        iniDA=inis.split('T')[0].split('-')
        iniTA=inis.split('T')[1].split(':')
        fimDA=fims.split('T')[0].split('-')
        fimTA=fims.split('T')[1].split(':')
        ini = datetime(int(iniDA[0]),int(iniDA[1]),int(iniDA[2]),int(iniTA[0]),int(iniTA[1]),0)
        fim = datetime(int(fimDA[0]),int(fimDA[1]),int(fimDA[2]),int(fimTA[0]),int(fimTA[1]),0)
        ini += timedelta(hours=3)
        fim += timedelta(hours=3)
        print(f'{ini}')
        print(f'{fim}')
        dadof = Evento.objects.filter(Q(date__gt=ini) & Q(date__lt=fim)).order_by('date')
        strinfy = ""
        
        for hf in dadof:
            hora = int(hf.date.hour)-3
            if hora<0:
                hora+=23  
            hf.date = f'{hora}:{hf.date.minute} {hf.date.day}/{hf.date.month}/{hf.date.year}'
            strinfy = f'{strinfy}{{"hora":"{hf.date}","Node":"{hf.node}","Tipo":"{hf.tipo}","Evento":"{hf.descricao}"}},'
        strinfy = "[" + strinfy[:len(strinfy)-1] + "]"
        return HttpResponse(strinfy)





def para_dict(obj):
    # Se for um objeto, transforma num dict
    if hasattr(obj, '__dict__'):
        obj = obj.__dict__

    # Se for um dict, lê chaves e valores; converte valores
    if isinstance(obj, dict):
        return { k:para_dict(v) for k,v in obj.items() }
    # Se for uma lista ou tupla, lê elementos; também converte
    elif isinstance(obj, list) or isinstance(obj, tuple):
        return [para_dict(e) for e in obj]
    # Se for qualquer outra coisa, usa sem conversão
    else: 
        return obj

class dict_to_obj(object):
    def __init__(self, d):
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
               setattr(self, a, [obj(x) if isinstance(x, dict) else x for x in b])
            else:
               setattr(self, a, obj(b) if isinstance(b, dict) else b)

class objectDict(dict):
    def __getattr__(self,name):
        return self.__getitem__(name)