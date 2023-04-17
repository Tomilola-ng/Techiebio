from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
from django.utils.timezone import now
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation

categories = (
    ('Bio','Bio'),
    ('Startup', 'Startup'),
)

class BioManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(category = 'Bio')

class StartupManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                      .filter(category = 'Startup')

class Article(models.Model, HitCountMixin):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.CharField(choices = categories, max_length=100, default='Bio')
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    content = RichTextField()
    about = models.CharField(max_length=50, default='Hidden from the Tech World')
    image = models.CharField(max_length=1000, default="https://firebasestorage.googleapis.com/v0/b/techiebio-f4784.appspot.com/o/blank-profile-picture-female.png?alt=media&token=e4c7b614-223d-483e-a251-e8b20aa7fc53")
    
    # Managers
    objects = models.Manager()
    bio_obj = BioManager()
    startup_obj = StartupManager()
    tags = TaggableManager()

    publish = models.DateTimeField(default=now)
    updated = models.DateTimeField(auto_now=True)

    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    share_count = models.PositiveIntegerField(default=0)
    
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
    ]
        
    def get_absolute_url(self):
        return reverse('detail_view', args=[self.slug] )


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} commented on '{self.article.title}'"

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='shares_history')
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} shared '{self.article.title}'"
    
