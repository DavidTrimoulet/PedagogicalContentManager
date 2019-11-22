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
        level_ = BloomLevel.objects.get(level=level)
        verb_ = BloomVerb.objects.get(verb=verb)
        family_ = BloomFamily.objects.get(family=family)
        BloomTaxonomy.objects.create(level=level_, verb=verb_, family=family_)

    @staticmethod
    def create_skill(verb="", text=""):
        taxonomy = BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=verb))
        Skill.objects.create(taxonomy=taxonomy, text=text)

    @staticmethod
    def create_skill_rubricks(verb="", text="", level_A="", level_B="",level_C="",level_D=""):
        skill = Skill.objects.get(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb=verb)), text=text)
        SkillRubricks.objects.create(skill=skill, level_A=level_A, level_B=level_B, level_C=level_C, level_D=level_D)

    @classmethod
    def setUpClass(cls):
        # add test data
        cls.create_bloom_verb(verb="Conceive")
        cls.create_bloom_verb(verb="Explain")
        cls.create_bloom_verb(verb="Describe")
        cls.create_bloom_verb(verb="Make")
        cls.create_bloom_level(level="Level1")
        cls.create_bloom_level(level="Level2")
        cls.create_bloom_family(family="Analyse")
        cls.create_bloom_family(family="Knowledge")
        cls.create_bloom_taxonomy(level="Level1", verb="Conceive", family="Analyse")
        cls.create_bloom_taxonomy(level="Level1", verb="Describe", family="Analyse")
        cls.create_bloom_taxonomy(level="Level2", verb="Explain", family="Knowledge")
        cls.create_skill(verb="Explain", text="elementary embedded systems")
        cls.create_skill(verb="Describe", text="electronic elementary component behaviour")
        cls.create_skill_rubricks(verb="Explain", text="elementary embedded systems",
                                  level_A="Can explain what are ALU, Register, Memory and IO",
                                  level_B="Can explain what are ALU, Register and Memory",
                                  level_C="Can explain what are ALU and Register",
                                  level_D="Can explain what is ALU")

    @classmethod
    def tearDownClass(cls):
        pass

class AppManagerTest(BaseViewTest):

# Bloom verb
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
# Bloom Level
    def test_put_one_bloom_level(self):
        response = self.client.put(
            reverse('bloom_level-all', kwargs={'version': "v1"}), data=json.dumps({"level": "Level3"}), content_type='application/json')
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

# Bloom Family
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

    def test_post_one_bloom_family_with_pk_1(self):
        response = self.client.post(
            reverse("bloom_families-detail", kwargs={"version": "v1", "pk": "1"})
        )
        expected = BloomFamily.objects.get(pk=1)
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

# Bloom Taxonomy
    def test_put_one_bloom_taxonomy(self):
        response = self.client.put(
            reverse('bloom_taxonomies-all', kwargs={'version': "v1"}), data=json.dumps({"level": "Level4", "verb": "Create", "family":"Analyse"}), content_type='application/json')
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

    def test_post_one_bloom_taxonomy_with_verb_(self):
        response = self.client.post(
            reverse("bloom_taxonomies-detail", kwargs={"version": "v1", "verb": "Conceive"})
        )
        expected = BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb="Conceive"))
        serialized = BloomTaxonomySerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_bloom_taxonomy_with_verb_Test(self):
        response = self.client.post(
            reverse("bloom_taxonomies-detail", kwargs={"version": "v1", "verb": "Test"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "BloomTaxonomy verb : Test does not exist")
        self.assertEqual(response.status_code, expected)
        
        
# Skill
    def test_put_one_skill(self):
        response = self.client.put(
            reverse('skill-all', kwargs={"version": "v1"}),
                                 data=json.dumps({"verb":"Conceive",
                                                  "text":"electronic elementary component behaviour"}),
                                 content_type='application/json')
        expected = Skill.objects.last()
        self.assertEqual(response.data["taxonomy"],  BloomTaxonomySerializer(expected.taxonomy).data)
        self.assertEqual(response.data["text"], expected.text)
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

    def test_post_one_skill_with_verb_Explain(self):
        response = self.client.post(
            reverse("skill-detail", kwargs={"version": "v1", "verb": "Explain"})
        )
        expected = Skill.objects.get(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb="Explain")))
        serialized = SkillSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_skill_with_verb_complain(self):
        response = self.client.post(
            reverse("skill-detail", kwargs={"version": "v1", "verb": "Complain"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "Skill with verb Complain does not exist")
        self.assertEqual(response.status_code, expected)

# Skill Rubriks
    def test_put_one_skill_rubriks(self):
        response = self.client.put(
            reverse('skill_rubricks-all', kwargs={"version": "v1"}),
                                          data=json.dumps({"verb":"Describe",
                                                           "text":"electronic elementary component behaviour",
                                                           "level_A": "Can explain Resistance, Impedance, Inductance and Capacitance",
                                                           "level_B": "Can explain Resistance, Impedance and Inductance",
                                                           "level_C": "Can explain Resistance and Impedance",
                                                           "level_D": "Can explain Resistance" }),
                                          content_type='application/json')
        expected = SkillRubricks.objects.last()
        self.assertEqual(response.data["skill"]["taxonomy"],  BloomTaxonomySerializer(expected.skill.taxonomy).data)
        self.assertEqual(response.data["skill"]["text"], SkillSerializer(expected.skill).data["text"])
        self.assertEqual(response.data["level_A"], expected.level_A)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_skill_rubriks(self):
        response = self.client.get(
            reverse("skill_rubricks-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = SkillRubricks.objects.all()
        serialized = SkillRubricksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_skill_rubricks_with_skill_Explain_electronic_elementary_component_behaviour(self):
        response = self.client.post(
            reverse("skill_rubricks-detail", kwargs={"version": "v1", "verb": "Explain", "text": "elementary embedded systems"})
        )
        expected = SkillRubricks.objects.get(skill=Skill.objects.get(taxonomy=BloomTaxonomy.objects.get(verb=BloomVerb.objects.get(verb="Explain")), text="elementary embedded systems"))
        serialized = SkillRubricksSerializer(expected, many=False)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_one_skill_rubricks_with_verb_complain(self):
        response = self.client.post(
            reverse("skill_rubricks-detail", kwargs={"version": "v1", "verb": "Describe", "text": "elementary embedded systems"})
        )
        expected = status.HTTP_404_NOT_FOUND
        self.assertEqual(response.data["message"], "SkillRubricks with verb Describe does not exist")
        self.assertEqual(response.status_code, expected)

#