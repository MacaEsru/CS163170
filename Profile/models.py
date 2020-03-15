from django.db import models
from django.utils import timezone


class City(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'City'

class Gender(models.Model):
    tipo = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'Gender'    

class Occupation(models.Model):
    tipo = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'Occupation'  

class State(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'State'    

class MaritalStatus(models.Model):
    tipo = models.CharField(max_length=254, null=False)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo
    
    class Meta:
        db_table = 'MaritalStatus' 

class Profile(models.Model):
    nombre = models.CharField(max_length=254, null=False)
    apellidoPaterno = models.CharField(max_length=254, null=False)
    apellidoMaterno = models.CharField(max_length=254, null=False)
    edad = models.IntegerField(null=False)
    ciudad = models.ForeignKey(City, on_delete = models.CASCADE)
    genero = models.ForeignKey(Gender, on_delete = models.CASCADE)
    ocupacion = models.ForeignKey(Occupation, on_delete = models.CASCADE)
    estado = models.ForeignKey(State, on_delete = models.CASCADE)
    estadoCivil = models.ForeignKey(MaritalStatus, on_delete = models.CASCADE)
    delete = models.BooleanField(default=False)
    create = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'Profile'