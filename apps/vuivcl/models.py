from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.core.exceptions import ValidationError
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill,Thumbnail
from .utils import Utils




#1. Post---
class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).all()
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.SET_NULL,null=True)
    category =models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    IMAGE = 'IM'
    YOUTUBE = 'YO'
    GIF = 'GI'
    LIST_TYPE = (
        (IMAGE,'IMAGE'),
        (YOUTUBE,'YOUTUBE'),
        (GIF,'GIF'),
    )
    post_type = models.CharField(max_length=2,choices=LIST_TYPE,default=None)
    viewed_number = models.IntegerField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_date= models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    @property
    def absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    @property
    def media(self):
        qs = Media.objects.filter(post=self)
        return qs
    @property
    def media_first(self):
        qs = Media.objects.filter(post=self).first()
        return qs

    class Meta:
        ordering = ["-created_date", "-updated_date"]

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = Utils.create_slug(instance)
pre_save.connect(pre_save_post_receiver, sender=Post)

#2. Media---
def upload_location(instance, filename):
    return "vuivcl/%s" % (filename)
class Media(models.Model):
    IMAGE = 'IM'
    YOUTUBE = 'YO'
    GIF = 'GI'
    LIST_TYPE = (
        (IMAGE,'IMAGE'),
        (YOUTUBE,'YOUTUBE'),
        (GIF,'GIF'),
    )
    media_type = models.CharField(max_length=2,choices=LIST_TYPE,default=IMAGE)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                                )
    image_thumb1 = ImageSpecField(source='image',
                                 processors=[Thumbnail(545)],
                                 format='JPEG',
                                 options={'quality': 100})
    image_thumb2 = ImageSpecField(source='image',
                                 processors=[ResizeToFill(348, 174)],
                                 format='JPEG',
                                 options={'quality': 100})
    image_thumb3 = ImageSpecField(source='image',
                                 processors=[Thumbnail(762)],
                                 format='JPEG',
                                 options={'quality': 100})
    youtube = models.URLField(null=True,blank=True)


    post = models.ForeignKey('Post', on_delete=models.CASCADE)



#3. Category---
class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    enabled = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = Utils.create_slug(instance)
pre_save.connect(pre_save_post_receiver, sender=Post)










