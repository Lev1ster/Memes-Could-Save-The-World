from rest_framework import serializers

from .models import Post, UserSubscribe, PostRead


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'text', 'pub_date', 'id_user']
        extra_kwargs = {
            'id_user': {'read_only': True}
        }


class UserSubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscribe
        fields = ['id_user', 'postSubscribe']


class PostReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostRead
        fields = ['id_user', 'id_post']
