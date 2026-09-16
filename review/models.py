from django.conf import settings
from django.db import models

from product.models import Product


class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='ratings', on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'user'), name='unique_product_user'),
        ]
        ordering = ('-created',)

    def __str__(self):
        return f'{self.product} - {self.rating} by {self.user}'
