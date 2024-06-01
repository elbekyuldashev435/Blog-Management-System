from django.db import models
from users.models import CustomUser
# Create your models here.


class Products(models.Model):
    image = models.ImageField(upload_to='all/image', blank=True, null=True)
    video = models.FileField(upload_to='all/video', blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return f"ID: {self.pk} | Title: {self.title} | Author: {self.author.username}"


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment = models.TextField()

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f"ID: {self.pk} | User: {self.user.username} | Product: {self.product.title}"


class Saved(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        db_table = 'saved'

    def __str__(self):
        return f"ID: {self.pk} | User: {self.user.username} | Product: {self.product.title}"