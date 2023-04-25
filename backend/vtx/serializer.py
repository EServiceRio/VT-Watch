from rest_framework import serializers
from .models import OS

class OsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OS
        fields = '__all__'