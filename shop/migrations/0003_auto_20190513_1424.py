# Generated by Django 2.2.1 on 2019-05-13 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190513_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='advance',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='battery',
            field=models.CharField(default='', max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='behind_camera',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cpu',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='front_camera',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='gpu',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='monitor',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='op_sys',
            field=models.CharField(default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rom',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
