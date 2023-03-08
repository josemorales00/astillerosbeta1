# Generated by Django 4.1.7 on 2023-03-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_lora_alter_testmeters_payload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
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
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medidores',
            fields=[
                ('id_med', models.BigAutoField(primary_key=True, serialize=False)),
                ('dev_nombre', models.CharField(max_length=15)),
                ('noserie', models.CharField(db_column='NoSerie', max_length=10)),
                ('deveui', models.CharField(db_column='DevEUI', max_length=20)),
                ('appeui', models.CharField(db_column='AppEUI', max_length=20)),
                ('rate', models.CharField(db_column='Rate', max_length=15)),
                ('appkey', models.CharField(db_column='AppKey', max_length=50)),
                ('devaddr', models.CharField(db_column='DevAddr', max_length=10)),
                ('appskey', models.CharField(db_column='AppSKey', max_length=50)),
                ('nwkskey', models.CharField(db_column='NwkSKey', max_length=50)),
                ('clase', models.CharField(db_column='Clase', max_length=10)),
                ('modo', models.CharField(db_column='Modo', max_length=10)),
            ],
            options={
                'db_table': 'medidores',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Lora',
        ),
    ]