from django.http import HttpResponse
from rest_framework.views import status

# Create your views here.

from rest_framework import generics
from .models import BloomVerb
from .serializers import BloomVerbSerializer
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


def index(request):
    return HttpResponse("Welcome to the competency repository")
