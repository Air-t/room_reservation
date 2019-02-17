from django.db import models


PHONE_CHOICES = (
    (0, 'Mobile'),
    (1, 'Home'),
    (2, 'Work'),
    (3, 'FAX'),
)

EMAIL_CHOICES = (
    (0, 'Mobile'),
    (1, 'Home'),
    (2, 'Work'),
)


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='avatar', blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Address(models.Model):
    city = models.CharField(max_length=128)
    street = models.CharField(max_length=128)
    home_no = models.CharField(max_length=64)
    apartment_no = models.CharField(max_length=64)
    zip_code = models.IntegerField(blank=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.street} street, " \
               f"{self.home_no}/{self.apartment_no}"


class Phone(models.Model):
    number = models.CharField(max_length=32)
    number_type = models.IntegerField(default=0, choices=PHONE_CHOICES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number} {self.number_type}"


class Email(models.Model):
    email = models.CharField(max_length=64)
    email_type = models.IntegerField(default=0, choices=EMAIL_CHOICES)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.email} {self.email_type}"


class Group(models.Model):
    group_name = models.CharField(max_length=128)
    person = models.ManyToManyField(Person)

    def __str__(self):
        return self.group_name
