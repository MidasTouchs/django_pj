# Generated by Django 5.2 on 2025-04-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_module_pages'),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='quizzes',
            field=models.ManyToManyField(to='quiz.quizzes'),
        ),
    ]
