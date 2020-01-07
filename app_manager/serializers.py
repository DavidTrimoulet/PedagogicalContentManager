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
    family = serializers.SlugRelatedField(many=False, read_only=True, slug_field='family')
    level = serializers.SlugRelatedField(many=False, read_only=True, slug_field='level')

    class Meta:
        model = BloomTaxonomy
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    taxonomy = BloomTaxonomySerializer(many=False, read_only=True)

    class Meta:
        model = Skill
        fields = '__all__'


class SkillRubricksSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=False, read_only=True)

    class Meta:
        model = SkillRubricks
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyWord
        fields = '__all__'


class ActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = '__all__'


class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = '__all__'


class ProblemContentSerializer(serializers.ModelSerializer):
    keyword = KeywordSerializer(many=True, read_only=True)
    skill = SkillSerializer(many=True, read_only=True)
    action_plan = ActionPlanSerializer(many=True, read_only=True)
    ressources = RessourceSerializer(many=True, read_only=True)

    class Meta:
        model = ProblemContent
        fields = '__all__'


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = '__all__'


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = HintAndAdvise
        fields = '__all__'


class ValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValidationQuestion
        fields = '__all__'

class HypothesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hypothesis
        fields = '__all__'
