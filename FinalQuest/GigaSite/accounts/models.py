#from accounts.models import *
from django.contrib.auth import get_user_model
from posts.models import *

def get_all_posts(self):
    posts = Post.objects.none()
    id_posts = PostRead.objects.filter(id_user = self).\
        values_list('id_post')
    
    for id in Post.objects.exclude(id_user = self).\
        values_list('id'):
        isExist = False

        for id_post_read in id_posts:
            if(id == id_post_read):
                isExist = True

        if isExist != True:
           posts |= Post.objects.filter(pk=id[0])            

    return posts.order_by('-pub_date')
        
def get_user_posts(self):
    return Post.objects.filter(id_user = self).order_by('-pub_date')

def get_all_subscribe_posts(self):
    posts = Post.objects.none()
    id_posts = UserSubscribe.objects.filter(id_user = self).\
        values_list('postSubscribe')
    
    for id in Post.objects.all().values_list('id'):
        isExist = False

        for id_post_read in id_posts:
            if(id == id_post_read):
                isExist = True

        if isExist != True:
           posts |= Post.objects.filter(pk=id[0])            

    return posts.order_by('-pub_date')

def get_all_read_posts(self):
    posts = Post.objects.none()
    id_posts = PostRead.objects.filter(id_user = self).\
        values_list('id_post')
    
    for id in Post.objects.all().\
        values_list('id'):
        isExist = False

        for id_post_read in id_posts:
            if(id != id_post_read):
                isExist = True

        if isExist != True:
           posts |= Post.objects.filter(pk=id[0])            

    return posts.order_by('-pub_date')

def get_all_users_post_subscribe(self):
    posts = Post.objects.none()
    id_posts = UserSubscribe.objects.filter(id_user = self).\
        values_list('postSubscribe')
    
    for id in id_posts:
        id_user = Post.objects.filter(pk=id[0]).\
            values_list('id_user')[0]

        posts |= get_user_posts(get_user_model().objects.\
            filter(pk = id_user[0])[0])            

    return posts.order_by('-pub_date')

get_user_model().add_to_class("get_all_posts",get_all_posts)
get_user_model().add_to_class("get_user_posts",get_user_posts)
get_user_model().add_to_class("get_all_subscribe_posts",get_all_subscribe_posts)
get_user_model().add_to_class("get_all_read_posts",get_all_read_posts)
get_user_model().add_to_class("get_all_users_post_subscribe",get_all_users_post_subscribe)