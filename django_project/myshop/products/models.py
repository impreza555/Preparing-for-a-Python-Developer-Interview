from django.db import models


class Suppliers(models.Model):
    """Поставщики товаров"""
    name = models.CharField(verbose_name='имя поставщика', max_length=128, unique=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['name']


MEASURE_UNIT_CHOICES = [
    ('шт.', 'штук'),
    ('кг.', 'килограмм'),
    ('лит.', 'литров'),
]


class Product(models.Model):
    """Продукты"""
    
    name = models.CharField(verbose_name='название', max_length=128)
    date = models.DateField(verbose_name='дата поступления')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    measure_unit = models.CharField(verbose_name='единица измерения', max_length=10, choices=MEASURE_UNIT_CHOICES)
    supplier = models.ForeignKey(Suppliers, verbose_name='поставщик', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} {self.price} {self.supplier}'
    
    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ['-date', 'name']
