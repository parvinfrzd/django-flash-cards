# Generated by Django 4.0.1 on 2022-02-05 22:34

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0002_category_status_alter_flashcard_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flashcards.category'),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 5, 22, 34, 51, 154106, tzinfo=utc)),
        ),
    ]
