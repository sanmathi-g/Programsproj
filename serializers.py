from rest_framework import serializers
from .models import programs,ProgCategory,ProgSeries

class programsSerializer(serializers.ModelSerializer):
    class Meta:
        model = programs
        fields = ['id', 'title','content','prog_series','prog_slug']
        depth = 1

class ProgCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgCategory
        fields = ['id','Category_title', 'Category_summary','Category_slug']

class ProgSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgSeries
        fields = ['id','prog_series', 'Category_title']
        depth = 1
