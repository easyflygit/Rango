from django.db import models
from django.template.defaultfilters import slugify
import re


class Category(models.Model):
    """Класс для категорий."""
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        """Сохраняет slug для URL"""
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        """Правильно прописывает категории во множественном числе."""
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Возвращает название категории."""
        return self.name


class Page(models.Model):
    """Класс для страниц"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        """Возвращает заголовок страницы."""
        return self.title

    def clean(self):
        """Проверяет правильность ввода ссылки на безопасный HTTPS"""
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # Strip away any leading http or https
        url = re.sub(r"http[s]:[\/]+", "", url)
        # If url is not empty and doesn't start with 'https://',
        # then prepend 'https://' as we want to make sure
        # we are accessing a secure site
        if url:
            url = f"https://{url}"
            cleaned_data['url'] = url
        return cleaned_data

