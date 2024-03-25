# Generated by Django 3.1.14 on 2024-01-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('brand', models.CharField(default='', max_length=255, verbose_name='品牌')),
                ('carName', models.CharField(default='', max_length=255, verbose_name='车名')),
                ('carImg', models.CharField(default='', max_length=255, verbose_name='图片链接')),
                ('saleVolume', models.CharField(default='', max_length=255, verbose_name='销量')),
                ('min_price', models.CharField(default='', max_length=255, verbose_name='最低价格')),
                ('max_price', models.CharField(default='', max_length=255, verbose_name='最高价格')),
                ('manufacturer', models.CharField(default='', max_length=255, verbose_name='厂商')),
                ('rank', models.CharField(default='', max_length=255, verbose_name='排名')),
                ('carModel', models.CharField(default='', max_length=255, verbose_name='车型')),
                ('energyType', models.CharField(default='', max_length=255, verbose_name='能源类型')),
                ('marketTime', models.CharField(default='', max_length=255, verbose_name='上市时间')),
                ('over_score', models.CharField(default='', max_length=255, verbose_name='综合评分')),
                ('appearance_score', models.CharField(default='', max_length=255, verbose_name='外观评分')),
                ('interior_score', models.CharField(default='', max_length=255, verbose_name='内饰评分')),
                ('configure_score', models.CharField(default='', max_length=255, verbose_name='配置评分')),
                ('spatial_score', models.CharField(default='', max_length=255, verbose_name='空间评分')),
                ('comfort_score', models.CharField(default='', max_length=255, verbose_name='舒适性评分')),
                ('manipulating_score', models.CharField(default='', max_length=255, verbose_name='操控评分')),
                ('motivation_score', models.CharField(default='',  max_length=255, verbose_name='动力评分')),
                ('comprehensive_evaluation', models.TextField(default='', verbose_name='综合评价')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'carInfo',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('username', models.CharField(default='', max_length=255, verbose_name='用户名')),
                ('password', models.CharField(default='', max_length=255, verbose_name='密码')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
