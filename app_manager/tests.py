from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.utils import json
from .models import *
from .serializers import *
from rest_framework.views import status

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_bloom_verb(verb=""):
        BloomVerb.objects.create(bloom_verb=verb)

    @staticmethod
    def create_bloom_level(level=""):
        BloomLevel.objects.create(bloom_level=level)

    @staticmethod
    def create_bloom_taxonomy(level="", verb=""):
        level = BloomLevel.objects.get(bloom_level=level)
        verb = BloomVerb.objects.get(bloom_verb=verb)
        bloom_taxonomy = BloomTaxonomy.objects.create(bloom_level=level, bloom_verb=verb)

    def setUp(self):
        # add test data
        self.create_bloom_verb("Create")
        self.create_bloom_verb("Explain")
        self.create_bloom_verb("Test")
        self.create_bloom_verb("Make")
        self.create_bloom_level("Level1")
        self.create_bloom_level("Level2")
        self.create_bloom_taxonomy("Level1", "Create")
        self.create_bloom_taxonomy("Level2", "Explain")


class BloomTest(BaseViewTest):

    def test_post_one_bloom_verb(self):
        response = self.client.post(
            reverse('bloom_verb-all', kwargs={'version': "v1"}), data=json.dumps({"bloom_verb": "Analyse"}), content_type='application/json')
        expected = BloomVerb.objects.last()
        self.assertEqual(response.data["bloom_verb"], expected.bloom_verb)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

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
        expected = BloomVerb.objects.get(pk=1)
        serialized = BloomVerbSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_bloom_verb_with_pk_10(self):
        response = self.client.get(
            reverse("bloom_verb-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.status_code, expected)

    def test_post_one_bloom_level(self):
        response = self.client.post(
            reverse('bloom_level-all', kwargs={'version': "v1"}), data=json.dumps({"bloom_level": "Level1"}), content_type='application/json')
        expected = BloomLevel.objects.last()
        self.assertEqual(response.data["bloom_level"], expected.bloom_level)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_bloom_level(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("bloom_level-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = BloomLevel.objects.all()
        serialized = BloomLevelSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_bloom_level_with_pk_1(self):
        response = self.client.get(
            reverse("bloom_level-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomLevel.objects.get(pk=1)
        serialized = BloomLevelSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_bloom_level_with_pk_10(self):
        response = self.client.get(
            reverse("bloom_level-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "BloomLevel with id: 10 does not exist")
        self.assertEqual(response.status_code, expected)

    def test_put_one_bloom_taxonomy(self):
        response = self.client.post(
            reverse('bloom_taxonomy-all', kwargs={'version': "v1"}), data=json.dumps({"bloom_level": "Level1", "bloom_verb": "Create"}), content_type='application/json')
        expected = BloomTaxonomy.objects.last()
        self.assertEqual(response.data["bloom_level"], expected.bloom_level.id)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
