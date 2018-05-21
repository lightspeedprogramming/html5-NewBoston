from django.db import models

# Create your models here.

class group(models.Model):
    num = models.IntegerField(default=0)

    def __str__(self):
        return "Group {0}".format(str(self.num))

class machine(models.Model):
    name = models.CharField(max_length=250)
    architecture = models.CharField(max_length=250)
    myGroup = models.ForeignKey(group)

    def __str__(self):
        return "{0}: Arch: {1}".format(self.name, self.architecture)
