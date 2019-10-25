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
    skill_verb = models.ForeignKey(BloomTaxonomy, on_delete=models.CASCADE, null=True)
    skill_text = models.CharField(max_length=1024)


class SkillLevel(models.Model):
    skill_name = models.OneToOneField(Skill, on_delete='cascade')
    skill_A = models.CharField(max_length=1024)
    skill_B = models.CharField(max_length=1024)
    skill_C = models.CharField(max_length=1024)
    skill_D = models.CharField(max_length=1024)


class CctlAnswer(models.Model):
    cctl_question_text = models.CharField(max_length=1024)


class CctlQuestion(models.Model):
    cctl_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    cctl_question_text = models.CharField(max_length=1024)
    cctl_question_answers = models.ManyToManyField(CctlAnswer)


class CCTL(models.Model):
    cctl_questions = models.ManyToManyField(CctlQuestion)


class ExerciseManipulation(models.Model):
    manipulation_text = models.CharField(max_length=1024)
    manipulation_image = models.CharField(max_length=256)


class Exercise(models.Model):
    exercise_skills = models.ForeignKey(Skill, on_delete='cascade', null=True )
    exercise_text = models.CharField(max_length=1024)
    exercise_image = models.CharField(max_length=256)
    exercise_solution = models.CharField(max_length=1024)
    exercise_manipulations = models.ForeignKey(ExerciseManipulation, on_delete='cascade', null=True)
    exercise_pub_date = models.DateTimeField('date published')


class Role(models.Model):
    role = models.CharField(max_length=256)


class Version(models.Model):
    version_number = models.IntegerField()
    version_text = models.IntegerField()
    version_author = models.OneToOneField(User, on_delete='cascade', null=True)
    version_pub_date = models.DateTimeField('date published')


class ValidationQuestion(models.Model):
    validation_question_text = models.CharField(max_length=1024)
    validation_question_answer = models.CharField(max_length=1024)
    validation_question_answer_schema = models.CharField(max_length=256)


class Resource(models.Model):
    resource_ref = models.CharField(max_length=1024)
    resource_image = models.CharField(max_length=256)


class KeyWord(models.Model):
    keyword = models.CharField(max_length=1024)
    definition = models.CharField(max_length=1024)
    definition_schema = models.CharField(max_length=256)


class Solution(models.Model):
    solution_text = models.CharField(max_length=1024)
    solution_image = models.CharField(max_length=256)


class Hypothesis(models.Model):
    Hypothesis_text = models.CharField(max_length=1024)
    Hypothesis_answer = models.CharField(max_length=1024)
    Hypothesis_answer_image = models.CharField(max_length=256)


class HintAndAdvise(models.Model):
    hint_and_advise_text = models.CharField(max_length=1024)


class Deliverable(models.Model):
    deliverable_text = models.CharField(max_length=1024)
    project_skills = models.ForeignKey(Skill, on_delete='cascade', null=True)


class Milestone(models.Model):
    milestone_date = models.DateField('date published')
    milestone_deliverables = models.ForeignKey(Deliverable, on_delete='cascade', null=True)


class Workshop(models.Model):
    workshop_title = models.CharField(max_length=256)
    workshop_text = models.CharField(max_length=1024)
    workshop_steps = models.ManyToManyField(Exercise)
    workshop_versions = models.ManyToManyField(Version)


class Problem(models.Model):
    problem_title = models.CharField(max_length=256)
    problem_text = models.CharField(max_length=1024)
    problem_keyword = models.ManyToManyField(KeyWord)
    problem_problem = models.CharField(max_length=1024)
    problem_skill = models.ManyToManyField(Skill)
    problem_hint_and_advise = models.OneToOneField(HintAndAdvise, on_delete='cascade', null=True)
    problem_action_plan = models.ManyToManyField(ActionPlan)
    problem_validation_questions = models.ManyToManyField(ValidationQuestion)
    problem_resources = models.ManyToManyField(Resource)
    problem_solution = models.ManyToManyField(Solution)
    problem_versions = models.ManyToManyField(Version)


class Project(models.Model):
    project_text = models.CharField(max_length=1024)
    project_problems = models.ManyToManyField(Problem)
    project_resources = models.ManyToManyField(Resource)
    project_milestones = models.ManyToManyField(Milestone)
    project_versions = models.ManyToManyField(Version)


