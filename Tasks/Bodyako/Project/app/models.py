from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    textarea = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'feedback form'
        verbose_name_plural = 'feedback forms'
 
