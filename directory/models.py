from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from taggit.managers import TaggableManager


# STATUS = ((0, "Draft"), (1, "Published"))


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


class Comment(models.Model):
    """
    Model class for a Comments on Resouces
    """
    resource = models.ForeignKey(
        Resource, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments_left")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"