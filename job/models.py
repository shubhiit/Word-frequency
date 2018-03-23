from django.db import models
from django.core.urlresolvers import reverse

class Words(models.Model):
    number_of_words = models.IntegerField(null=True)

    def get_absolute_url(self):
        return reverse('job:result', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.number_of_words)
