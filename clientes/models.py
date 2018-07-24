from django.db import models

class Doc(models.Model):
    num_doc = models.CharField(max_length=9);
    def __str__(self):
        return self.num_doc


class Person(models.Model):
    firstName = models.CharField(max_length=20);
    lastName = models.CharField(max_length=20);
    age = models.IntegerField();
    salary = models.DecimalField(max_digits=8, decimal_places=2);
    bio = models.TextField();
    photo = models.ImageField(upload_to='client_photos', null=True, blank=True);
    # client_photos é a pasta que vai ser criada, null e blank é pra deixar opcional
    document = models.OneToOneField(Doc, null=True, blank=True, on_delete=models.CASCADE);

    def __str__(self):
        return self.firstName;
