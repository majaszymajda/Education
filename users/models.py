import imp
import profile
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from attributes.models import Interests, Categories, Badges, ToLernCategories


class User(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]



class Profile(models.Model):
    class Gender(models.TextChoices):
        WOMAN = _("Woman")
        MAN = _("Man")
        OTHER = _("Other")


    class Wants(models.TextChoices):
        LEARNING = _("learning")
        TEACHING = _("teaching")
        DEVELOPING = _("developing")

    gender = models.CharField(
        max_length=20, choices=Gender.choices, default=Gender.WOMAN
    )
    is_admin = models.BooleanField(default=True)
    is_company = models.BooleanField(default=True)
    date_of_birth = models.DateField()
    interests = models.ForeignKey(Interests, on_delete=models.CASCADE, null=True)
    to_learn = models.ForeignKey(ToLernCategories, on_delete=models.CASCADE, null=True)
    badges = models.ForeignKey(Badges, on_delete=models.CASCADE, null=True)

    # competencies = models.ManyToManyField(Skill, related_name="workstations")
    modification_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name="profile")
    user_wants = models.CharField(
        max_length=20, choices=Wants.choices, default=Wants.LEARNING
    )

    # path_of_development = models.ForeignKey(PathOfDevelopment, on_delete=models.CASCADE, null=True)