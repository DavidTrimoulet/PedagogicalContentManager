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
        BloomVerb.objects.create(verb=verb)

    @staticmethod
    def create_bloom_level(level=""):
        BloomLevel.objects.create(level=level)

    @staticmethod
    def create_bloom_family(family=""):
        BloomFamily.objects.create(family=family)
    
    @staticmethod
    def create_bloom_taxonomy(level="", verb="", family=""):
        level = BloomLevel.objects.get(level=level)
        verb = BloomVerb.objects.get(verb=verb)
        family = BloomFamily.objects.get(family=family)
        BloomTaxonomy.objects.create(level=level, verb=verb, family=family)

    @staticmethod
    def create_skill(verb="", text=""):
        verb = BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=verb))
        Skill.objects.create(skill_verb=verb, skill_text=text)

    def setUp(self):
        # add test data
        self.create_bloom_verb(verb="Conceive")
        self.create_bloom_verb(verb="Explain")
        self.create_bloom_verb(verb="Describe")
        self.create_bloom_verb(verb="Make")
        self.create_bloom_level(level="Level1")
        self.create_bloom_level(level="Level2")
        self.create_bloom_family(family="Analyse")
        self.create_bloom_family(family="Knowledge")
        self.create_bloom_taxonomy(level="Level1", verb="Conceive", family="Analyse")
        self.create_bloom_taxonomy(level="Level2", verb="Explain", family="Knowledge")
        self.create_bloom_taxonomy(level="Level2", verb="Explain", family="Knowledge")
        self.create_skill(verb="Conceive", text="elementary embedded systems")


class BloomVerbTest(BaseViewTest):

    def test_put_one_bloom_verb(self):
        response = self.client.put(
            reverse('bloom_verb-all', kwargs={'version': "v1"}), data=json.dumps({"verb": "Explain"}), content_type='application/json')
        expected = BloomVerb.objects.last()
        self.assertEqual(response.data["verb"], expected.verb)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_bloom_verb(self):
        response = self.client.get(
            reverse("bloom_verb-all", kwargs={"version": "v1"})
        )
        expected = BloomVerb.objects.all()
        serialized = BloomVerbSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_verb_with_pk_1(self):
        response = self.client.post(
            reverse("bloom_verb-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomVerb.objects.get(pk=1)
        serialized = BloomVerbSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_verb_with_pk_10(self):
        response = self.client.post(
            reverse("bloom_verb-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.status_code, expected)

class BloomLevelTest(BaseViewTest):
    def test_put_one_bloom_level(self):
        response = self.client.put(
            reverse('bloom_level-all', kwargs={'version': "v1"}), data=json.dumps({"level": "Level1"}), content_type='application/json')
        expected = BloomLevel.objects.last()
        self.assertEqual(response.data["level"], expected.level)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_bloom_level(self):
        response = self.client.get(
            reverse("bloom_level-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = BloomLevel.objects.all()
        serialized = BloomLevelSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_level_with_pk_1(self):
        response = self.client.post(
            reverse("bloom_level-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomLevel.objects.get(pk=1)
        serialized = BloomLevelSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_level_with_pk_10(self):
        response = self.client.post(
            reverse("bloom_level-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "BloomLevel with id: 10 does not exist")
        self.assertEqual(response.status_code, expected)

class BloomFamilyTest(BaseViewTest):
    def test_put_one_bloom_family(self):
        response = self.client.put(
            reverse('bloom_families-all', kwargs={'version': "v1"}), data=json.dumps({"family": "Evaluate"}), content_type='application/json')
        expected = BloomFamily.objects.last()
        self.assertEqual(response.data["family"], expected.family)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_bloom_family(self):
        response = self.client.get(
            reverse("bloom_families-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = BloomFamily.objects.all()
        serialized = BloomFamilySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_family_with_pk_3(self):
        response = self.client.post(
            reverse("bloom_families-detail", kwargs={"version": "v1", "pk": "3"})
        )
        expected = BloomFamily.objects.get(pk=3)
        serialized = BloomFamilySerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_family_with_pk_10(self):
        response = self.client.post(
            reverse("bloom_families-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "BloomFamily with id: 10 does not exist")
        self.assertEqual(response.status_code, expected)

class BloomTaxonomyTest(BaseViewTest):
    def test_put_one_bloom_taxonomy(self):
        response = self.client.put(
            reverse('bloom_taxonomies-all', kwargs={'version': "v1"}), data=json.dumps({"level": "Level5", "verb": "Create", "family":"Analyse"}), content_type='application/json')
        expected = BloomTaxonomy.objects.last()
        self.assertEqual(response.data["level"], expected.level.level)
        self.assertEqual(response.data["verb"], expected.verb.verb)
        self.assertEqual(response.data["family"], expected.family.family)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_bloom_taxonomy(self):
        response = self.client.get(
            reverse("bloom_taxonomies-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = BloomTaxonomy.objects.all()
        serialized = BloomTaxonomySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_taxonomy_with_pk_1(self):
        response = self.client.post(
            reverse("bloom_taxonomies-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomTaxonomy.objects.get(pk=1)
        serialized = BloomTaxonomySerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_taxonomy_with_pk_10(self):
        response = self.client.post(
            reverse("bloom_taxonomies-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "BloomTaxonomy with id: 10 does not exist")
        self.assertEqual(response.status_code, expected)
        
        
class SkillTest(BaseViewTest):
    def test_put_one_skill(self):
        response = self.client.put(
            reverse('skill-all', kwargs={"version": "v1"}), data=json.dumps({"verb":"Describe", "skill":"electronic elementary component behaviour"}), content_type='application/json')
        expected = Skill.objects.last()
        print(response.data)
        self.assertEqual(response.data["skill_verb"], expected.skill_verb)
        self.assertEqual(response.data["text_text"], expected.skill_text)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_skill(self):
        response = self.client.get(
            reverse("skill-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Skill.objects.all()
        serialized = SkillSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_skill_with_pk_1(self):
        response = self.client.post(
            reverse("skill-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = Skill.objects.get(pk=1)
        serialized = SkillSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_skill_with_pk_10(self):
        response = self.client.post(
            reverse("skill-detail", kwargs={"version": "v1", "pk": "10"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "Skill with id: 10 does not exist")
        self.assertEqual(response.status_code, expected)