# Generated by Django 4.2.7 on 2023-11-23 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Presentacion', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='libro',
            name='Presentacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas.presentacion'),
        ),
    ]
