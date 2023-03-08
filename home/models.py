from django.db import models

# Create your models here.
class TestMeters(models.Model):
    n_serie = models.BigIntegerField(db_column='N_serie')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nombre_medidor = models.CharField(db_column='Nombre medidor', max_length=14)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appeui = models.CharField(db_column='AppEUI', max_length=18)  # Field name made lowercase.
    deveui = models.CharField(db_column='DevEUI', max_length=16)  # Field name made lowercase.
    payload = models.CharField(db_column='Payload', max_length=20)  # Field name made lowercase.
    #payload = models.BigIntegerField(db_column='Payload')  # Field name made lowercase.
    payload_decodificado = models.CharField(db_column='Payload decodificado', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ultima_revision = models.CharField(db_column='Ultima revision', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'test_meters'

class Datos(models.Model):
    id = models.BigAutoField(primary_key=True)
    deveui = models.CharField(db_column='DevEUI', max_length=20)  # Field name made lowercase.
    devaddr = models.CharField(db_column='devAddr', max_length=15)  # Field name made lowercase.
    datos = models.CharField(db_column='Datos', max_length=100)  # Field name made lowercase.
    consumo = models.DecimalField(db_column='Consumo', max_digits=10, decimal_places=4)  # Field name made lowercase.
    fechamed = models.DateTimeField(db_column='FechaMed', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha')  # Field name made lowercase.

    class Meta:
        db_table = 'datos'
        app_label = 'home'


class Medidores(models.Model):
    id_med = models.BigAutoField(primary_key=True)
    dev_nombre = models.CharField(max_length=15)
    noserie = models.CharField(db_column='NoSerie', max_length=10)  # Field name made lowercase.
    deveui = models.CharField(db_column='DevEUI', max_length=20)  # Field name made lowercase.
    appeui = models.CharField(db_column='AppEUI', max_length=20)  # Field name made lowercase.
    rate = models.CharField(db_column='Rate', max_length=15)  # Field name made lowercase.
    appkey = models.CharField(db_column='AppKey', max_length=50)  # Field name made lowercase.
    devaddr = models.CharField(db_column='DevAddr', max_length=10)  # Field name made lowercase.
    appskey = models.CharField(db_column='AppSKey', max_length=50)  # Field name made lowercase.
    nwkskey = models.CharField(db_column='NwkSKey', max_length=50)  # Field name made lowercase.
    clase = models.CharField(db_column='Clase', max_length=10)  # Field name made lowercase.
    modo = models.CharField(db_column='Modo', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medidores'