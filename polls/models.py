import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
LEVEL_CHOICES = [
    ("easy", "easy"),
    ("normal","normal"),
    ("hard","hard"),
]

class PublisheedBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(pub_date__lt=timezone.now())



class Question(models.Model):
    question_text = models.CharField(max_length=300,verbose_name=_("question text"))
    pub_date = models.DateTimeField(verbose_name=_("publication date"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("created"))
    modified = models.DateTimeField(auto_now=True, verbose_name=_("modified"))
    is_active = models.BooleanField(default=True, verbose_name=_("is_active"))
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, null=True, blank=True, verbose_name=_("level"))
    question_image = models.ImageField(null=True, blank=True, upload_to="questionimages/%Y/%m/%d", verbose_name=_("question_image"))

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

    objects = models.Manager() #all wszystkie
    published = PublisheedBookManager() # prefiltrowac elementy i potem mozna budować i odpowlywac sie do zapytania



    class Meta:
        verbose_name = _("Question")




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
