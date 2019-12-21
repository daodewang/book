from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):
    """
    用户,
    """
    APIKey = models.CharField(max_length=30, verbose_name='apikey', default='abcdefgh')
    money = models.IntegerField(default=10, verbose_name='余额')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    书籍信息
    """
    title = models.CharField(max_length=30, verbose_name='书名', default='')
    isbn = models.CharField(max_length=30, verbose_name='isbn', default='')
    auther = models.CharField(max_length=20, verbose_name='作者', default='')
    publish = models.CharField(max_length=30, verbose_name='出版社', default='')
    rate = models.FloatField(default=0, verbose_name='花瓣评分')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Type(models.Model):
    """
    图书类别
    """
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
        (4, '四级类目')
    )

    name = models.CharField(default='', max_length=30, verbose_name='类别名', help_text='类别名')
    code = models.CharField(default='', max_length=30, verbose_name='类别码', help_text='类别码')
    desc = models.CharField(default='', max_length=30, verbose_name='类别描述', help_text='类别描述')
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name='类别', help_text='类别')
    parent_category = models.ForeignKey('self', null=True, blank=True, verbose_name='父类类别', help_text='父类别',
                                        related_name='sub_cat', on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name='是否导航', help_text='是否导航')

    class meta:
        verbose_name = '图书类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

