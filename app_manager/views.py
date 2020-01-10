from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework.views import status
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
import re
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

    def post(self, request, *args, **kwargs):
        try:
            bloom_verb = self.queryset.get(pk=request.data["pk"])
            return Response(self.serializer_class(bloom_verb).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomVerb with id: {} does not exist".format(request.data["pk"])
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

    def post(self, request, *args, **kwargs):
        try:
            bloom_level = self.queryset.get(pk=request.data["pk"])
            return Response(self.serializer_class(bloom_level).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomLevel with id: {} does not exist".format(request.data["pk"])
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

    def post(self, request, *args, **kwargs):
        try:
            bloom_family = self.queryset.get(pk=request.data["pk"])
            return Response(self.serializer_class(bloom_family).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomFamily with id: {} does not exist".format(request.data["pk"])
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

    def post(self, request, *args, **kwargs):
        try:
            bloom_taxonomy = BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=request.data["verb"]))
            return Response(BloomTaxonomySerializer(bloom_taxonomy).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "BloomTaxonomy verb : {} does not exist".format(request.data["verb"])
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

    def post(self, request, *args, **kwargs):
        try:
            skill = Skill.objects.get(
                taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=request.data["verb"])))
            return Response(self.serializer_class(skill).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Skill with verb {} does not exist".format(request.data["verb"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SkillRubricksView(generics.ListAPIView):
    queryset = SkillRubricks.objects.all()
    serializer_class = SkillRubricksSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        skill, skill_created = Skill.objects.get_or_create(
            taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=request.data["verb"])),
            text=request.data["text"])
        skill_rubricks, created = SkillRubricks.objects.get_or_create(skill=skill)
        skill_rubricks.level_A = request.data["level_a"]
        skill_rubricks.level_B = request.data["level_b"]
        skill_rubricks.level_C = request.data["level_c"]
        skill_rubricks.level_D = request.data["level_d"]
        skill_rubricks.save()
        if created:
            return Response(data=SkillRubricksSerializer(skill_rubricks).data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=SkillRubricksSerializer(skill_rubricks).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            skill_rubricks = SkillRubricks.objects.get(skill=Skill.objects.get(
                taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=request.data["verb"])),
                text=request.data["text"]))
            return Response(self.serializer_class(skill_rubricks).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "SkillRubricks with verb {} does not exist".format(request.data["verb"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ProblemsView(generics.ListAPIView):
    queryset = Problem.objects.all()

    def get(self, request, *args, **kwargs):
        return Response(data=ProblemSerializer(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        print(request.data)
        if 'title' in request.data.keys():
            cleanr = re.compile('<.*?>')
            title = re.sub(cleanr, '', request.data['title'])
            self.queryset.filter(pk=request.data['id']).update(title=title)
        else:
            problem_content = ProblemContent.objects.get(pk=request.data['id'])
            problem_content.problem_text=request.data['problem_text']
            problem_content.save()
        return Response(data='', status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            problem_content, created = ProblemContent.objects.get_or_create(
                problem=Problem.objects.get(title=request.data['problem']))
            return Response(data=ProblemContentSerializer(problem_content).data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(request.data["problem"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class VersionView(generics.ListAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            version = Version.objects.get(problem=Problem.objects.get(title=kwargs["problemTitle"]).id)
            return Response(self.serializer_class(version).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class SolutionView(generics.ListAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            solution = Solution.objects.get(problem=Problem.objects.get(title=kwargs["problemTitle"]).id)
            return Response(self.serializer_class(solution).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class HintView(generics.ListAPIView):
    queryset = HintAndAdvise.objects.all()
    serializer_class = HintSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            hint = HintAndAdvise.objects.get(problem=Problem.objects.get(title=kwargs["problemTitle"]).id)
            return Response(self.serializer_class(hint).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class ValidationView(generics.ListAPIView):
    queryset = ValidationQuestion.objects.all()
    serializer_class = ValidationSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            validation = ValidationQuestion.objects.get(problem=Problem.objects.get(title=kwargs["problemTitle"]).id)
            return Response(self.serializer_class(validation).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class HypothesisView(generics.ListAPIView):
    queryset = Hypothesis.objects.all()
    serializer_class = HypothesisSerializer

    def get(self, request, *args, **kwargs):
        return Response(data=self.serializer_class(self.queryset.all(), many=True).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        try:
            hypothesis = Hypothesis.objects.get(problem=Problem.objects.get(title=kwargs["problemTitle"]).id)
            return Response(self.serializer_class(hypothesis).data)
        except ObjectDoesNotExist:
            return Response(
                data={
                    "message": "Problem with title \"{}\" does not exist".format(kwargs["title"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class UploadImage(generics.ListAPIView):

    def post(self, request, *args, **kwargs):
        print("data ", request.FILES['image'])
        print(request.data['image'])
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url( filename)
        return Response(data={"url": uploaded_file_url}, status=status.HTTP_201_CREATED);
