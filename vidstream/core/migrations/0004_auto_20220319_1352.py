# Generated by Django 3.2.9 on 2022-03-19 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220319_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='runtime',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=9999, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.video'),
        ),
        migrations.AlterField(
            model_name='video',
            name='details',
            field=models.TextField(max_length=99999, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='tviews',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.category'),
        ),
    ]
