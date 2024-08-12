from django.db import models
from django.contrib.auth import get_user_model

from taggit.managers import TaggableManager


User = get_user_model()

class Product(models.Model):
    """
    Art Product Model.
    """

    # initial fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/img/")
    title = models.CharField(max_length=50)
    description = models.TextField()

    # tag field
    tag = TaggableManager()

    def __str__(self) -> str:
        return self.title
