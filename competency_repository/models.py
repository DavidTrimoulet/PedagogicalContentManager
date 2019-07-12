from django.db import models


class ActionPlan(models.Model):
    action_plan_steps = models.CharField(max_length=1024)



class BloomVerb(models.Model):
    bloom_verb = models.CharField(max_length=256)


class BloomLevel(models.Model):
    bloom_level = models.CharField(max_length=256)


class BloomTaxonomy(models.Model):
    level = models.ManyToManyField(BloomLevel)
    taxonomy_verb = models.ManyToManyField(BloomVerb)


class SkillFamily(models.Model):
    family_text = models.CharField(max_length=256)
    bloom_ref = models.ManyToManyField(BloomTaxonomy)


class Skill(models.Model):
    skill_verb = models.ManyToManyField(BloomTaxonomy)
    skill_text = models.CharField(max_length=1024)
    skill_family = models.ManyToManyField(SkillFamily)


class SkillLevel(models.Model):
    skill_name = models.OneToOneField(Skill, on_delete='cascade')
    skill_A = models.CharField(max_length=1024)
    skill_B = models.CharField(max_length=1024)
    skill_C = models.CharField(max_length=1024)
    skill_D = models.CharField(max_length=1024)


class CctlQuestion(models.Model):
    cctl_skill = models.ManyToManyField(Skill)
    cctl_question_text = models.CharField(max_length=1024)
    cctl_question_answers = models.CharField(max_length=1024)


class CCTL(models.Model):
    cctl_questions = models.ManyToManyField(CctlQuestion)


class ExerciseManipulation(models.Model):
    manipulation = models.CharField(max_length=1024)


class Exercise(models.Model):
    exercise_text = models.CharField(max_length=1024)
    exercise_solution = models.CharField(max_length=1024)
    exercise_manipulations = models.ManyToManyField(ExerciseManipulation)
    exercise_pub_date = models.DateTimeField('date published')


class Project(models.Model):
    project_text = models.CharField(max_length=1024)


class Role(models.Model):
    role = models.CharField(max_length=256)


class ValidationQuestion(models.Model):
    validation_question_text = models.CharField(max_length=1024)
    validation_question_answer = models.CharField(max_length=1024)


class Prosit(models.Model):
    prosit_text = models.CharField(max_length=1024)
    prosit_skill = models.ManyToManyField(Skill)
    prosit_action_plan = models.ManyToManyField(ActionPlan)
    prosit_validation_questions = models.ManyToManyField(ValidationQuestion)