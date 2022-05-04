from django.contrib import admin

# Register your models here.
from .models import Post
from .models import UserSubscribe
from .models import PostRead

admin.site.register(Post)
admin.site.register(UserSubscribe)
admin.site.register(PostRead)
