# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TestMeters(models.Model):
    n_serie = models.BigIntegerField(db_column='No. serie')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nombre_medidor = models.CharField(db_column='Nombre medidor', max_length=14)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appeui = models.CharField(db_column='AppEUI', max_length=18)  # Field name made lowercase.
    deveui = models.CharField(db_column='DevEUI', max_length=16)  # Field name made lowercase.
    payload = models.BigIntegerField(db_column='Payload')  # Field name made lowercase.
    payload_decodificado = models.CharField(db_column='Payload decodificado', max_length=32)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ultima_revision = models.CharField(db_column='Ultima revision', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'test_meters'
