# Generated by Django 3.0.6 on 2020-08-26 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad', '0011_auto_20200815_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_product', to='ad.Ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
