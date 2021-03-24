# Generated by Django 3.1.7 on 2021-03-23 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='cards.card'),
        ),
    ]