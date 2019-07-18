from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import BloomVerb
from .serializers import BloomVerbSerializer
from rest_framework.views import status

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bloom_verb(verb=""):
        BloomVerb.objects.create(bloom_verb=verb)

    @staticmethod
    def create_bloom_verb(verb=""):
        BloomVerb.objects.create(bloom_verb=verb)

    def setUp(self):
        # add test data
        self.create_bloom_verb("create")
        self.create_bloom_verb("explain")
        self.create_bloom_verb("test")
        self.create_bloom_verb("make")


class GetAllBloomVerbTest(BaseViewTest):

    def test_get_all_bloom_verb(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("bloom_verb-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = BloomVerb.objects.all()
        serialized = BloomVerbSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_bloom_verb_with_pk_1(self):
        response = self.client.get(
            reverse("bloom_verb-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomVerb.objects.get(pk="1")
        serialized = BloomVerbSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_bloom_verb_with_pk_10(self):
        response = self.client.get(
            reverse("bloom_verb-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.status_code, expected)