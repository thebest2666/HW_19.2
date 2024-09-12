from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="описание продукта",
        help_text="Введите описание продукта",
    )
    photo = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="изображение продукта",
        help_text="Вставьте изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="категория продукта",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.CharField(
        max_length=50, verbose_name="цена продукта", help_text="Введите цену продукта"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания продукта",
        help_text="Введите дату создания продукта",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "created_at"]

    def __str__(self):
        return self.name
