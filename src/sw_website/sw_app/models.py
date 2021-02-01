from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns



from tinymce.models import HTMLField


class Story(models.Model):
    name = models.CharField(max_length=100)

class Card(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    #content = HTMLField()
    who = models.CharField(max_length=100)
    what = models.CharField(max_length=100)
    why = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    time_bound = models.CharField(max_length=100)

class Confirmation(models.Model):
    story = models.OneToOneField(Story, on_delete=models.CASCADE)
    creator = models.CharField(max_length=100)
    approver = models.CharField(max_length=100)
    date = models.DateField(max_length=100)
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
    description = models.TextField(help_text= "Bir ürün iş listesinde üstte olan kullanıcı hikayeleri ilk geliştirilecek hikayelerdir. Bu yüzden bu hikayeler, ekibin anlayabilmesi ve büyüklüğünü ölçümleyebilmesi için yeteri kadar detaylandırılmalıdır. Yeteri kadar dememin bir sebebi var. Her şeyin en ince detayına kadar açıklanması değil de geliştirici ekibin ölçümleyebilmesi ve planlayabilmesine imkan sağlayacak kadar detaylandırılmış olması yeterlidir.")
    story_input = models.CharField(max_length=100)
    story_output = models.CharField(max_length=100)
    data_source = models.CharField(max_length=100)
    formula = models.CharField(max_length=100)
    internal_apis = models.CharField(max_length=100)
    external_apis = models.CharField(max_length=100)

class Resource(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    resource = models.BooleanField()
