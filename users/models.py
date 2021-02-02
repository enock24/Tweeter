from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# Tweet model
class Tweet(models.Model):
    message = models.TextField(max_length=250)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        # return reverse('compose', kwargs={'pk': self.pk})
        return reverse('tweet-detail', kwargs={'pk': self.pk})

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    description = models.TextField(default='Something something something', max_length=250)

    def __str__(self):
        return self.user.username

    #####  ORM COMMANDS #####

    # - User.objects.all()

    # - Tweets.objects.all()

    # - me = User.objects.get(username='BobbyHen')

    # - Tweets.objects.create(author=me, message='Another test')