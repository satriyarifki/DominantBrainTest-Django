# Generated by Django 3.2.10 on 2021-12-20 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruangtest', '0003_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='num',
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ruangtest.test'),
        ),
    ]