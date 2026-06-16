from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):

    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=120, blank=True, null=True)
    done = models.BooleanField(default=False)

    created_at = models.DateField(auto_now_add=True, auto_created=True, editable=False)
    deadline = models.DateField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.name

    def change_status(self):
        self.done = not self.done
        self.save()
