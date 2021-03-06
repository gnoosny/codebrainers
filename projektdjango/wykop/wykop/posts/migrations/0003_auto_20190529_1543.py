# Generated by Django 2.2.1 on 2019-05-29 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vote',
            name='value',
            field=models.IntegerField(choices=[(1, '+'), (-1, '-')]),
        ),
    ]
