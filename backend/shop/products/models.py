from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Product(models.Model):

    title = models.CharField(max_length=100, verbose_name=_("Название"), unique=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=[MinValueValidator(1), ],
        verbose_name=_("Цена")
    )

    def __str__(self):
        return f"{self.title}: {self.price}"

    class Meta:
        ordering = ["-id",]
        verbose_name = _("Товар")
        verbose_name_plural = _("Товары")