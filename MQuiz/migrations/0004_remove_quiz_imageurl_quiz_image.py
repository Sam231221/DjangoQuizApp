# Generated by Django 4.0 on 2022-04-20 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQuiz', '0003_remove_quiz_image_quiz_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='imageurl',
        ),
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(max_length=400, null=True, upload_to=''),
        ),
    ]
