from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Themes(models.Model):
    name = models.CharField(max_length=35)
    articles = models.ManyToManyField('Article', through='ArticleTheme',
                                      related_name='themes'
                                      )

    def __str__(self):
        return self.name



class ArticleTheme(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    theme = models.ForeignKey('Themes', on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    class Meta:
        ordering = ['theme__name']
