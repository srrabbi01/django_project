# Generated by Django 4.0.4 on 2022-05-19 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_shop', '0002_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop_name',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=264, null=True),
        ),
    ]
