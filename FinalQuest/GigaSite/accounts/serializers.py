from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    total_posts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'total_posts'
        ]

    def get_total_posts(self, user):
        return Post.objects.filter(id_user=user.id).count()    