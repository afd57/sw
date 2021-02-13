from django.db import models
# Used to generate URLs by reversing the URL patterns
from django.urls import reverse
from tinymce.models import HTMLField
from mdeditor.fields import MDTextField
from tinymce.models import HTMLField
from django_quill.fields import QuillField

class Epic(models.Model):
    name = models.TextField()
    overview = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Story(models.Model):
    title = models.CharField(max_length=200)
    story_type = models.CharField(max_length=100)
    epic = models.OneToOneField(Epic, on_delete=models.CASCADE)


class Card(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    #content = HTMLField()
    who = models.TextField(help_text="As a .....")
    what = models.TextField(help_text="I want .....")
    why = models.TextField(help_text="So that .....")
    priority = models.IntegerField(help_text="0 is most important 100 is least important")
    time_bound = models.DateField()


class Confirmation(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    creator = models.CharField(max_length=100)
    approver = models.CharField(max_length=100)
    date = models.DateField()
    note = models.CharField(max_length=100)


class Independent(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    state = models.BooleanField()


class Small(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    state = models.BooleanField()


class AcceptanceCriteria(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    criteria = models.CharField(max_length=100)

class DetailedAppropriately(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    description = QuillField(help_text="Bir ürün iş listesinde üstte olan kullanıcı hikayeleri ilk geliştirilecek hikayelerdir. Bu yüzden bu hikayeler, ekibin anlayabilmesi ve büyüklüğünü ölçümleyebilmesi için yeteri kadar detaylandırılmalıdır. Yeteri kadar dememin bir sebebi var. Her şeyin en ince detayına kadar açıklanması değil de geliştirici ekibin ölçümleyebilmesi ve planlayabilmesine imkan sağlayacak kadar detaylandırılmış olması yeterlidir.")
    #description = HTMLField()
    end_point = models.TextField()
    story_input = models.TextField()
    story_output = QuillField()
    data_source = QuillField()
    formula = models.TextField()
    internal_apis = models.TextField()
    external_apis = models.TextField()
    authantication = models.TextField()
    max_response_time = models.TextField()


class Resource(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    resource = models.TextField()

class Related(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
