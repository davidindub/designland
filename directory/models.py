from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


class Resource(models.Model):
    """
    Model class for design resources added to the directory
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    url = models.URLField(default="")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="resources_added")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    thumbnail = CloudinaryField("image", default="placeholder")
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    upvotes = models.ManyToManyField(
        User, related_name="upvoted_resources", blank=True)
    bookmarks = models.ManyToManyField(
        User, related_name="bookmarked_resources", blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_upvotes(self):
        return self.upvotes.count()


class Profile(models.Model):
    """
    Model class for user profiles
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username_twitter = models.CharField(max_length=15, null=True)
    username_github = models.CharField(max_length=39, null=True)

    def __str__(self):
        return self.user.username
    
    def number_resources_added(self):
        return self.user.resources_added.count()

    def total_upvotes_received(self):
        total = 0
        for resource in self.user.resources_added.all():
            total = total + resource.number_upvotes()
        return total

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
            instance.profile.save()
    