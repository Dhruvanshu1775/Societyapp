# Generated by Django 3.2.7 on 2021-09-27 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('execution', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseno',
            name='user_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('timedatemixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='userdata.timedatemixin')),
                ('house_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='execution.houseno')),
                ('s_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skey', to=settings.AUTH_USER_MODEL)),
                ('user_key', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('userdata.timedatemixin',),
        ),
    ]
