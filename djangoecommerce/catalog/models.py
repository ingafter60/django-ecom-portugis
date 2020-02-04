from django.db import models


class Category(models.Model):
    name = models.CharField('nome', max_length=100)
    slug = models.SlugField('identificador', max_length=100)
    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField('nome', max_length=100)
    slug = models.SlugField('identificador', max_length=100)
    category = models.ForeignKey('Category', verbose_name='categoria')
    description = models.TextField('descrição', blank=True)
    price = models.DecimalField('preço', decimal_places=2, max_digits=8)
    created = models.DateTimeField('criado em', auto_now_add=True)
    modified = models.DateTimeField('modificado em', auto_now=True)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'
        ordering = ['name', ]

    def __str__(self):
        return self.name