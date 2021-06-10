# Generated by Django 3.1.7 on 2021-06-10 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('booking_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='booking.booking')),
                ('periods', models.IntegerField()),
                ('name', models.CharField(max_length=120)),
            ],
            bases=('booking.booking',),
        ),
        migrations.AddField(
            model_name='booking',
            name='court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.court'),
        ),
    ]