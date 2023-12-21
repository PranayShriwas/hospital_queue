from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    urgency = models.IntegerField(default=0)  # Urgency level, higher values mean higher priority
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
