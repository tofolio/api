from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    related_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class CommunityPost(Post):
    community = models.ForeignKey(User, on_delete=models.CASCADE)


class PostUplaod(models.Model):
    image = models.ImageField(upload_to="/post-upload")


class Reaction(models.Model):
    class Reactions(models.Choices):
        UP = "UP","UP"
        DOWN = "DOWN","DOWN"
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.CharField(choices=Reactions.choices, max_length=20)
    reacted_at = models.DateTimeField(auto_now_add=True)


class SavedPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)