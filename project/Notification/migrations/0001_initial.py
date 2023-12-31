# Generated by Django 4.1.4 on 2023-01-24 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Profile', '0002_skillslist'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('seen', models.BooleanField(default=False)),
                ('action', models.IntegerField()),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_noti', to='Profile.profile')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_noti', to='Profile.profile')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Notification.notificationtype')),
            ],
        ),
    ]
