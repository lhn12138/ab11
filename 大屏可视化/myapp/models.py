from django.db import models

# Create your models here.
class CarInfo(models.Model):
    id = models.AutoField('id', primary_key=True)
    brand = models.CharField('品牌',max_length=255,default='')
    carName = models.CharField('车名', max_length=255, default='')
    carImg = models.CharField('图片链接', max_length=255, default='')
    saleVolume = models.CharField('销量', max_length=255, default='')
    min_price = models.CharField('最低价格', max_length=255, default='')
    max_price = models.CharField('最高价格', max_length=255, default='')
    manufacturer = models.CharField('厂商', max_length=255, default='')
    rank = models.CharField('排名', max_length=255, default='')
    carModel = models.CharField('车型', max_length=255, default='')
    energyType = models.CharField('能源类型', max_length=255, default='')
    marketTime = models.CharField('上市时间', max_length=255, default='')
    over_score = models.CharField('综合评分', max_length=255, default='')
    appearance_score = models.CharField('外观评分', max_length=255, default='')
    interior_score = models.CharField('内饰评分', max_length=255, default='')
    configure_score = models.CharField('配置评分', max_length=255, default='')
    spatial_score = models.CharField('空间评分', max_length=255, default='')
    comfort_score = models.CharField('舒适性评分', max_length=255, default='')
    manipulating_score = models.CharField('操控评分', max_length=255, default='')
    motivation_score = models.CharField('动力评分', max_length=255, default='')
    comprehensive_evaluation = models.CharField('综合评价', max_length=999999, default='')
    createTime=models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        db_table = "carInfo"

#用户
class User(models.Model):
    id = models.AutoField('id', primary_key=True)
    username = models.CharField('用户名', max_length=255, default='')
    password = models.CharField('密码', max_length=255, default='')
    createTime = models.DateTimeField('创建时间', auto_now_add=True)
    class Meta:
        db_table = "user"
