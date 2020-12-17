from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)


def item_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'items/item_{0}/{1}'.format(instance.item.id, filename)


class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=False, null=False)
    user_phone = models.CharField(max_length=12, null=False, blank=False)
    location = models.ForeignKey(Location,  on_delete=models.CASCADE)
    description = models.TextField(max_length=600, blank=False, null=False)
    price = models.IntegerField(blank=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.name


class Item_Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    img = models.ImageField(upload_to=item_directory_path)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.item.name


class Profile(models.Model):
    # user = models.ForeignKey(User, null=False, blank=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    img = models.ImageField(upload_to=user_directory_path, default="", blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'],location=Location.objects.first())


post_save.connect(create_profile, sender=User)


class Favorite_item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.user.username