from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver

def blog_image_path(instance,filename):
    return f'blogs/{instance.title}/{filename}'

class Blog(models.Model):
    title = models.CharField(verbose_name='title',max_length=100)
    text = RichTextField()
    image = models.ImageField(upload_to=blog_image_path)
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True)

    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ('-created_at',)
    

@receiver(pre_save,sender=Blog)
def slugify_title(sender,instance,*args, **kwargs):
    instance.slug = slugify(instance.title)


