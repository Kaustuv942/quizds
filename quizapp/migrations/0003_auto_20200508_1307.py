# Generated by Django 3.0.6 on 2020-05-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0002_books_myusers_series'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'ordering': ['day', 'order']},
        ),
        migrations.AlterModelOptions(
            name='myusers',
            options={'ordering': ['-pointsfactor', 'lastcorrectans']},
        ),
        migrations.AddField(
            model_name='books',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='movies',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='myusers',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='day',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='myusers',
            name='lastcorrectans',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
