from django.db import models

# Create your models here.
class Predict(models.Model):
    carName = models.CharField('车名', max_length=255, default=''),
    brand = models.CharField('品牌', max_length=255, default=''),
    years = models.CharField('年月', max_length=255, default=''),
    monthly_sales=models.CharField('月销量', max_length=255, default=''),
    monthly_rank = models.CharField('当月销量排名', max_length=255, default=''),
    manufacturer_share = models.CharField('占厂商份额', max_length=255, default=''),
    manufacturer_rank = models.CharField('在厂商排名', max_length=255, default=''),
    model_rank = models.CharField('在车型排名', max_length=255, default='')


    class Meta:
        db_table = "cleaned_data6"