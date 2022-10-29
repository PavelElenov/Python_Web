from django.db import models

from petstagram.main_app.validators import validate_name, validate_email


class Profile(models.Model):
    GENDERS = [(x, x) for x in ['Male', 'Female', "Do not show"]]

    first_name = models.CharField(
        max_length=30,
        validators=[validate_name],
    )
    last_name = models.CharField(
        max_length=30,
        validators=[validate_name],
    )
    picture = models.ImageField(upload_to='images')
    date_of_birth = models.DateField()
    description = models.TextField(
        null=True,
        blank=True,
    )
    email = models.CharField(
        max_length=30,
        unique=True,
        validators=[validate_email],
    )
    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=[x for x in GENDERS],
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    TYPES = [(x, x) for x in ["Cat", "Dog", "Bunny", "Parrot", "Fish", "Other"]]

    name = models.CharField(
        max_length=30,
    )
    type = models.CharField(
        max_length=max(len(x) for x, _ in TYPES),
        choices=[x for x in TYPES]
    )
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        unique_together = ('name', 'user')


class PetsPhoto(models.Model):
    photo = models.ImageField()
    tagged_pets = models.ManyToManyField(
        Pet,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    date_and_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    likes = models.IntegerField(
        default=0,
    )

