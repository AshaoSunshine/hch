# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-29 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewProductTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_model', models.IntegerField(verbose_name='产品型号')),
                ('pro_name', models.CharField(max_length=20, verbose_name='产品名称')),
                ('pro_version', models.CharField(max_length=20, verbose_name='产品版本')),
            ],
            options={
                'verbose_name': '新增产品',
                'verbose_name_plural': '新增产品',
                'db_table': 'df_new_product',
            },
        ),
        migrations.CreateModel(
            name='ProductPerformTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=20, verbose_name='产品名称')),
                ('pro_version', models.CharField(max_length=20, verbose_name='产品版本')),
                ('pro_pict', models.ImageField(upload_to='', verbose_name='产品图片')),
            ],
            options={
                'verbose_name': '产品展示',
                'verbose_name_plural': '产品展示',
                'db_table': 'df_product_perform',
            },
        ),
        migrations.CreateModel(
            name='ProductPictureTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_pict', models.ImageField(upload_to='', verbose_name='产品图片')),
            ],
            options={
                'verbose_name': '产品图片',
                'verbose_name_plural': '产品图片',
                'db_table': 'df_product_picture',
            },
        ),
        migrations.CreateModel(
            name='ProductPriceTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_version', models.CharField(max_length=20, verbose_name='产品版本')),
                ('hardware_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='硬件成本')),
                ('fir_software_cost', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='首次软件成本')),
                ('deve_cycle', models.DateField(verbose_name='开发周期')),
                ('single_hard_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单次硬性成本')),
                ('single_cost_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='单次成本合计')),
                ('batch_cost_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='批量成本合计')),
                ('cost_prop', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='成本比例')),
                ('actual_exte', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='实际对外')),
                ('agent_prop', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='代理比例')),
                ('profit_shar', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='利润分成')),
                ('exte_profit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='对外利润')),
                ('actual_profit', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='实际利润')),
                ('profit_require', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='利润要求')),
                ('pro_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='产品售价')),
                ('actual_profit_margin', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='实际利润率')),
                ('exte_profit_margin', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='对外利润率')),
            ],
            options={
                'verbose_name': '产品售价',
                'verbose_name_plural': '产品售价',
                'db_table': 'df_product_price',
            },
        ),
        migrations.CreateModel(
            name='ProductRecordTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_model', models.CharField(max_length=10, verbose_name='产品型号')),
                ('pro_name', models.CharField(max_length=20, verbose_name='产品名称')),
                ('pro_version', models.CharField(max_length=20, verbose_name='产品版本')),
                ('deve_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='研发成本')),
                ('batch_cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='批量成本')),
                ('pro_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='产品售价')),
                ('fill_in_date', models.DateField(verbose_name='填报时间')),
                ('update_date', models.DateField(verbose_name='更新时间')),
                ('persion', models.CharField(max_length=20, verbose_name='负责人')),
                ('fill_in_state', models.CharField(max_length=10, verbose_name='填报状态')),
                ('operation', models.CharField(max_length=10, verbose_name='操作')),
            ],
            options={
                'verbose_name': '产品记录',
                'verbose_name_plural': '产品记录',
                'db_table': 'df_product_record',
            },
        ),
        migrations.CreateModel(
            name='ProductTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=20, verbose_name='产品名称')),
                ('pro_version', models.CharField(max_length=20, verbose_name='产品版本')),
                ('pro_pict', models.ImageField(upload_to='', verbose_name='产品图片')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'df_product',
            },
        ),
        migrations.CreateModel(
            name='ProductVersionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver_name', models.CharField(max_length=20, verbose_name='版本名称')),
            ],
            options={
                'verbose_name': '产品版本',
                'verbose_name_plural': '产品版本',
                'db_table': 'df_product_version',
            },
        ),
        migrations.CreateModel(
            name='RotationProductTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=20, verbose_name='产品名称')),
                ('pro_pict', models.CharField(max_length=20, verbose_name='产品图片')),
            ],
            options={
                'verbose_name': '首页轮播产品图片',
                'verbose_name_plural': '首页轮播产品图片',
                'db_table': 'df_rotation_product',
            },
        ),
    ]
