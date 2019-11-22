from django.http import HttpResponse
from rest_framework.views import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response

class BloomVerbView(generics.ListAPIView):

    queryset = BloomVerb.objects.all()
    serializer_class = BloomVerbSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        bloom_verb = BloomVerb.objects.create(verb=request.data["verb"])
        bloom_verb.save()
        return Response(data=self.serializer_class(bloom_verb).data, status=status.HTTP_201_CREATED)


class BloomVerbDetailView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = BloomVerbSerializer
    queryset = BloomVerb.objects.all()

    def post(self, request, *args, **kwargs):
        try :
            bloom_verb = self.queryset.get(pk=kwargs["pk"])
            return Response(self.serializer_class(bloom_verb).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomVerb with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BloomLevelView(generics.ListAPIView):

    queryset = BloomLevel.objects.all()
    serializer_class = BloomLevelSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        bloom_level = BloomLevel.objects.create(level=request.data["level"])
        bloom_level.save()
        return Response(data=self.serializer_class(bloom_level).data, status=status.HTTP_201_CREATED)


class BloomLevelDetailView(generics.ListAPIView):

    queryset = BloomLevel.objects.all()
    serializer_class = BloomLevelSerializer

    def post(self, request, *args, **kwargs):
        try:
            bloom_level = self.queryset.get(pk=kwargs["pk"])
            return Response(self.serializer_class(bloom_level).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomLevel with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BloomFamilyView(generics.ListAPIView):

    queryset = BloomFamily.objects.all()
    serializer_class = BloomFamilySerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        bloom_family = BloomFamily.objects.create(family=request.data["family"])
        bloom_family.save()
        return Response(data=self.serializer_class(bloom_family).data, status=status.HTTP_201_CREATED)


class BloomFamilyDetailView(generics.ListAPIView):

    queryset = BloomFamily.objects.all()
    serializer_class = BloomFamilySerializer

    def post(self, request, *args, **kwargs):
        try:
            bloom_family = self.queryset.get(pk=kwargs["pk"])
            return Response(self.serializer_class(bloom_family).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomFamily with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BloomTaxonomyView(generics.ListAPIView):

    queryset = BloomTaxonomy.objects.all()
    serializer_class = BloomTaxonomySerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        bloom_level, created = BloomLevel.objects.get_or_create(level=request.data["level"])
        bloom_verb, created = BloomVerb.objects.get_or_create(verb=request.data["verb"])
        bloom_family, created = BloomFamily.objects.get_or_create(family=request.data["family"])
        bloom_taxonomy = BloomTaxonomy.objects.create(verb=bloom_verb, level=bloom_level, family=bloom_family)
        bloom_taxonomy.save()
        return Response(data=BloomTaxonomySerializer(bloom_taxonomy).data, status=status.HTTP_201_CREATED)


class BloomTaxonomyDetailView(generics.ListAPIView):

    serializer_class = BloomTaxonomySerializer

    def post(self, request, *args, **kwargs):
        try :
            bloom_taxonomy = BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=kwargs["verb"]))
            return Response(BloomTaxonomySerializer(bloom_taxonomy).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomTaxonomy verb : {} does not exist".format(kwargs["verb"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SkillView(generics.ListAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        bloom_verb = BloomVerb.objects.get(verb=request.data["verb"])
        taxonomy = BloomTaxonomy.objects.get(verb=bloom_verb)
        skill = Skill.objects.create(taxonomy=taxonomy, text=request.data["text"])
        skill.save()
        return Response(data=SkillSerializer(skill).data, status=status.HTTP_201_CREATED)


class SkillDetailView(generics.ListAPIView):
    serializer_class = SkillSerializer

    def post(self, request, *args, **kwargs):
        try :
            skill = Skill.objects.get(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=kwargs["verb"])))
            return Response(self.serializer_class(skill).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Skill with verb {} does not exist".format(kwargs["verb"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SkillRubricksView(generics.ListAPIView):

    queryset = SkillRubricks.objects.all()
    serializer_class = SkillRubricksSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        skill, skill_created = Skill.objects.get_or_create(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=request.data["verb"])), text=request.data["text"])
        skill_rubricks, created = SkillRubricks.objects.get_or_create(skill=skill)
        skill_rubricks.level_A=request.data["level_A"]
        skill_rubricks.level_B=request.data["level_B"]
        skill_rubricks.level_C=request.data["level_C"]
        skill_rubricks.level_D=request.data["level_D"]
        skill_rubricks.save()
        if created :
            return Response(data=SkillRubricksSerializer(skill_rubricks).data, status=status.HTTP_201_CREATED)
        else :
            return Response(data=SkillRubricksSerializer(skill_rubricks).data, status=status.HTTP_200_OK)


class SkillRubricksDetailView(generics.ListAPIView):
    serializer_class = SkillRubricksSerializer

    def post(self, request, *args, **kwargs):
        try :
            skill_rubricks = SkillRubricks.objects.get(skill=Skill.objects.get(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=kwargs["verb"])), text=kwargs["text"]))
            return Response(self.serializer_class(skill_rubricks).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "SkillRubricks with verb {} does not exist".format(kwargs["verb"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

class ProblemsView(generics.ListAPIView):

    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass


class ProblemsDetailView(generics.ListAPIView):
    serializer_class = ProblemSerializer

    def post(self, request, *args, **kwargs):
        try :
            problem = Problem.objects.get(title=kwargs["title"])
            return Response(self.serializer_class(problem).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )