from django.db import models


class Interests(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=20, default="programing"
    )
    is_active = models.BooleanField(default=True)


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=20, default="programing"
    )
    is_active = models.BooleanField(default=True)


class Badges(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=20, default="programing"
    )
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)


class ToLernCategories(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=20, default="programing"
    )

    is_active = models.BooleanField(default=True)

