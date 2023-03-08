# Generated by Django 4.1.7 on 2023-03-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_testmeters_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lora',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('deveui', models.CharField(db_column='DevEUI', max_length=20)),
                ('devaddr', models.CharField(db_column='devAddr', max_length=15)),
                ('datos', models.CharField(db_column='Datos', max_length=100)),
                ('consumo', models.DecimalField(db_column='Consumo', decimal_places=4, max_digits=10)),
                ('fechamed', models.DateTimeField(blank=True, db_column='FechaMed', null=True)),
                ('fecha', models.DateTimeField(db_column='Fecha')),
            ],
            options={
                'db_table': 'datos',
            },
        ),
        migrations.AlterField(
            model_name='testmeters',
            name='payload',
            field=models.CharField(db_column='Payload', max_length=20),
        ),
    ]