from rest_framework import serializers
from .models import programs



class programsSerializer(serializers.ModelSerializer):
    class Meta:
        model = programs
        fields = ['id', 'title']