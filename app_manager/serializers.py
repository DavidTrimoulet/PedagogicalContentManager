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


class BloomFamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = BloomFamily
        fields = '__all__'


class BloomTaxonomySerializer(serializers.ModelSerializer):
    verb = serializers.SlugRelatedField(many=False, read_only=True, slug_field='verb')
    family = serializers.SlugRelatedField(many=False,read_only=True, slug_field='family')
    level = serializers.SlugRelatedField(many=False,read_only=True, slug_field='level')

    class Meta:
        model = BloomTaxonomy
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    skill_verb = BloomTaxonomySerializer(many=False, read_only=True)

    class Meta:
        model = Skill
        fields = '__all__'
