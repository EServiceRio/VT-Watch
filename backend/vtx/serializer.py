from rest_framework import serializers
from .models import OS
from .models import Gateway, Node, NodeSetup, Evento, Hist

class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = '__all__'

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class NodeSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeSetup
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class HistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hist
        fields = '__all__'