from rest_framework import serializers
from .models import *


class BloomVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloomVerb
        fields = '__all__'

class BloomLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloomLevel
        fields = '__all__'


class BloomTaxonomySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloomTaxonomy
        fields = '__all__'