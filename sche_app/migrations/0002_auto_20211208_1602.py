# Generated by Django 3.2.9 on 2021-12-08 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sche_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=150)),
                ('unit', models.CharField(max_length=150)),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='schedule',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sche_app.task'),
        ),
    ]
