from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _



class User(AbstractUser):

    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]



class Profile(models.Model):
    class Sexes(models.TextChoices):
        WOMAN = _("Woman")
        MAN = _("Man")
        OTHER = _("Other")

    sex = models.CharField(
        max_length=20, choices=Sexes.choices, default=Sexes.WOMAN
    )
    is_admin = models.BooleanField(default=True)
    is_company = models.BooleanField(default=True)
    date_of_birth = models.DateTimeField()
    # interests = models.ForeignKey(Interest, on_delete=models.CASCADE, null=True)
    # competencies = models.ManyToManyField(Skill, related_name="workstations")
    modification_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    # path_of_development = models.ForeignKey(PathOfDevelopment, on_delete=models.CASCADE, null=True)