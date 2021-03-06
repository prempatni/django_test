# Generated by Django 3.0.6 on 2020-05-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_auto_20200515_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='airport',
            options={'verbose_name_plural': 'airport'},
        ),
        migrations.AlterModelOptions(
            name='flight',
            options={'verbose_name_plural': 'flight'},
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.Flight')),
            ],
            options={
                'verbose_name_plural': 'passenger',
            },
        ),
    ]
