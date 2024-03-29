# Generated by Django 2.2.5 on 2019-09-02 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='Agent_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='agent',
            name='Phone_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='agent',
            name='bucket_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='agent',
            name='team_leader_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Agent.Agent'),
        ),
    ]
