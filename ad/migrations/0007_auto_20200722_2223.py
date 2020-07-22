# Generated by Django 3.0.6 on 2020-07-22 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0006_auto_20200617_2121'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category_images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('i', 'LikeNew'), ('Good Condition', 'GoodCondition'), ('Bad Condition', 'BadCondition')], max_length=15, null=True),
        ),
    ]