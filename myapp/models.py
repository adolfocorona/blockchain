from django.db import models

class Login(models.Model):
    login_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    last_login_time = models.DateTimeField(null=True, blank=True)

    # Indica a Django que esta tabla ya está creada en la base de datos
    class Meta:
        managed = False
        db_table = 'login'  

class Transferencia(models.Model):
    transferencia_id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    transferencia_enviada = models.ForeignKey('login', on_delete=models.CASCADE, related_name='transferencia_enviada')
    transferencia_recibida = models.ForeignKey('login', on_delete=models.CASCADE, related_name='transferencia_recibida')

    class Meta:
        managed = False
        db_table = 'transferencia'

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    clabe_bancaria = models.CharField(max_length=45)
    login = models.ForeignKey('login', on_delete=models.CASCADE, related_name='clients', null=True)

    class Meta:
        managed = False
        db_table = 'clients'

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    clabe_bancaria = models.CharField(max_length=45)
    login = models.ForeignKey('login', on_delete=models.CASCADE, related_name='employees', null=True)

    class Meta:
        managed = False
        db_table = 'employees'

