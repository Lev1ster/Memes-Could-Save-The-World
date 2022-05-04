from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
	id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	title_text = models.CharField(null=False, max_length=50)
	main_text = models.TextField()
	pub_date = models.DateTimeField('Date published')
	
class UserSubscribe(models.Model):
	id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	postSubscribe = models.ManyToManyField(Post, blank=True)
	
class PostRead(models.Model):
	id_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	isRead = models.BooleanField(default=False)
