from django.http import HttpResponse
from rest_framework.views import status

# Create your views here.

from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.response import Response


class BloomVerbView(generics.ListAPIView):

    queryset = BloomVerb.objects.all()
    serializer_class = BloomVerbSerializer

    def post(self, request, *args, **kwargs):
        bloom_verb = BloomVerb.objects.create(bloom_verb=request.data["bloom_verb"])
        return Response(data=BloomVerbSerializer(bloom_verb).data, status=status.HTTP_201_CREATED)


class BloomVerbDetailView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = BloomVerbSerializer

    def get(self, request, *args, **kwargs):
        try :
            bloom_verb = BloomVerb.objects.get(pk=kwargs["pk"])
            return Response(BloomVerbSerializer(bloom_verb).data)
        except BloomVerb.DoesNotExist:
            return Response(
                data={
                    "message": "BloomVerb with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BloomLevelView(generics.ListAPIView):

    queryset = BloomLevel.objects.all()
    serializer_class = BloomLevelSerializer

    def post(self, request, *args, **kwargs):
        bloom_level = BloomLevel.objects.create(bloom_level=request.data["bloom_level"])
        return Response(data=BloomLevelSerializer(bloom_level).data, status=status.HTTP_201_CREATED)


class BloomLevelDetailView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = BloomLevelSerializer

    def get(self, request, *args, **kwargs):
        try :
            bloom_level = BloomLevel.objects.get(pk=kwargs["pk"])
            return Response(BloomLevelSerializer(bloom_level).data)
        except BloomVerb.DoesNotExist:
            return Response(
                data={
                    "message": "BloomLevel with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class BloomTaxonomyView(generics.ListAPIView):

    queryset = BloomTaxonomy.objects.all()
    serializer_class = BloomTaxonomySerializer

    def post(self, request, *args, **kwargs):
        bloom_taxonomy = BloomTaxonomy.objects.create()
        bloom_taxonomy.bloom_level.set(BloomLevel.objects.filter(bloom_level=request.data["bloom_level"]))
        bloom_taxonomy.bloom_verb.set(BloomVerb.objects.filter(bloom_verb=request.data["bloom_verb"]))
        return Response(data=BloomTaxonomySerializer(bloom_taxonomy).data, status=status.HTTP_201_CREATED)


class BloomTaxonomyDetailView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    serializer_class = BloomVerbSerializer

    def get(self, request, *args, **kwargs):
        try :
            bloom_verb = BloomVerb.objects.get(pk=kwargs["pk"])
            return Response(BloomVerbSerializer(bloom_verb).data)
        except BloomVerb.DoesNotExist:
            return Response(
                data={
                    "message": "BloomVerb with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )


def index(request):
    return HttpResponse("Welcome to the competency repository")
