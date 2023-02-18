from django.db import models


class Sensor(models.Model):

    TYPE = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
    ]

    name = models.CharField(max_length=2000)
    type = models.CharField(max_length=1, choices=TYPE, default="1")

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=2000)
    temperature = models.IntegerField(null=True)
    humidity = models.IntegerField(null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

