from django.db import models


class Team(models.Model):
    title = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    team = models.ManyToManyField(Team, related_name='persons')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
