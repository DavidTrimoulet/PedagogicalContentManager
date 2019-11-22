from django.db import models
from django.contrib.auth.models import User


class NewCenturySkill(models.Model):
    new_century_skill = models.CharField(max_length=1024)


class InvestigationMethod(models.Model):
    investigation_method = models.CharField(max_length=1024)


class InvolvingContext(models.Model):
    involving_context = models.CharField(max_length=1024)


class APPMetaData(models.Model):
    new_century_skills = models.ManyToManyField(NewCenturySkill)
    investigation_methods = models.ManyToManyField(InvestigationMethod)
    involving_contexts = models.ManyToManyField(InvolvingContext)


class ActionPlan(models.Model):
    action_plan_steps = models.CharField(max_length=1024)


class BloomVerb(models.Model):
    verb = models.CharField(max_length=256)


class BloomLevel(models.Model):
    level = models.CharField(max_length=256)


class BloomFamily(models.Model):
    family = models.CharField(max_length=256)


class BloomTaxonomy(models.Model):
    level = models.ForeignKey(BloomLevel, on_delete=models.CASCADE, null=True)
    verb = models.ForeignKey(BloomVerb,  on_delete=models.CASCADE, null=True)
    family = models.ForeignKey(BloomFamily,  on_delete=models.CASCADE, null=True)


class Skill(models.Model):
    taxonomy = models.ForeignKey(BloomTaxonomy, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=1024)


class SkillRubricks(models.Model):
    skill = models.ForeignKey(Skill, on_delete='cascade')
    level_A = models.CharField(max_length=1024)
    level_B = models.CharField(max_length=1024)
    level_C = models.CharField(max_length=1024)
    level_D = models.CharField(max_length=1024)


class CctlAnswer(models.Model):
    question_text = models.CharField(max_length=1024)


class CctlQuestion(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=1024)
    answers = models.ManyToManyField(CctlAnswer)


class CCTL(models.Model):
    questions = models.ManyToManyField(CctlQuestion)


class ExerciseManipulation(models.Model):
    manipulation_text = models.CharField(max_length=1024)
    manipulation_image = models.CharField(max_length=256)


class Exercise(models.Model):
    skills = models.ForeignKey(Skill, on_delete='cascade', null=True )
    text = models.CharField(max_length=1024)
    image = models.CharField(max_length=256)
    solution = models.CharField(max_length=1024)
    manipulations = models.ForeignKey(ExerciseManipulation, on_delete='cascade', null=True)
    pub_date = models.DateTimeField('date published')


class Role(models.Model):
    role = models.CharField(max_length=256)


class Resource(models.Model):
    ref = models.CharField(max_length=1024)
    image = models.CharField(max_length=256)


class KeyWord(models.Model):
    keyword = models.CharField(max_length=1024)
    definition = models.CharField(max_length=1024)
    definition_schema = models.CharField(max_length=256)


class Deliverable(models.Model):
    text = models.CharField(max_length=1024)
    skills = models.ForeignKey(Skill, on_delete='cascade', null=True)


class Milestone(models.Model):
    date = models.DateField('date published')
    deliverable = models.ForeignKey(Deliverable, on_delete='cascade', null=True)


class Workshop(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1024)
    steps = models.ManyToManyField(Exercise)


class Problem(models.Model):
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=1024)
    keyword = models.ManyToManyField(KeyWord)
    skill = models.ManyToManyField(Skill)
    action_plan = models.ManyToManyField(ActionPlan)
    resources = models.ManyToManyField(Resource)

class Version(models.Model):
    problem = models.ForeignKey(Problem, on_delete='cascade', null=True)
    number = models.IntegerField()
    text = models.CharField(max_length=256)
    author = models.OneToOneField(User, on_delete='cascade', null=True)
    pub_date = models.DateTimeField('date published')

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete='cascade', null=True)
    text = models.CharField(max_length=1024)
    image = models.CharField(max_length=256)

class ValidationQuestion(models.Model):
    problem = models.ForeignKey(Problem, on_delete='cascade', null=True)
    text = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    answer_schema = models.CharField(max_length=256)

class Hypothesis(models.Model):
    problem = models.ForeignKey(Problem, on_delete='cascade', null=True)
    text = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    answer_image = models.CharField(max_length=256)

class HintAndAdvise(models.Model):
    problem = models.ForeignKey(Problem, on_delete='cascade', null=True)
    text = models.CharField(max_length=1024)

class Project(models.Model):
    project_text = models.CharField(max_length=1024)
    project_problems = models.ManyToManyField(Problem)
    project_resources = models.ManyToManyField(Resource)
    project_milestones = models.ManyToManyField(Milestone)
    project_versions = models.ManyToManyField(Version)


