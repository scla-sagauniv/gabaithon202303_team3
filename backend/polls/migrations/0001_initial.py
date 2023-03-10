# Generated by Django 4.1.7 on 2023-03-02 08:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Garbage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lat', models.FloatField(default='0.0')),
                ('lng', models.FloatField(default='0.0')),
                ('image', models.ImageField(upload_to='')),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
