from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.email


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level_choices = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    ]
    level = models.CharField(max_length=15, choices=level_choices, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.level})"


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class CV(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField()

    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    contacts = models.OneToOneField(ContactInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
