# Generated by Django 4.1.4 on 2023-01-20 01:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Network', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thirdconnections',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='thirdconnections',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='secondconnections',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='secondconnections',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='follow',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='firstconnections',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='firstconnections',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='connectionrequest',
            name='reciever',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='Profile.profile'),
        ),
        migrations.AddField(
            model_name='connectionrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='Profile.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('profile', 'follower')},
        ),
        migrations.AlterUniqueTogether(
            name='connectionrequest',
            unique_together={('sender', 'reciever')},
        ),
    ]
