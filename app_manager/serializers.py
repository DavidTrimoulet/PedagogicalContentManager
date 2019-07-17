from rest_framework import serializers
from .models import BloomVerb


class BloomVerbSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloomVerb
        fields = '__all__'