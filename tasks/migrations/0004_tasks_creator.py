# Generated by Django 3.1.5 on 2021-01-15 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20210116_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tasks.creator'),
        ),
    ]
