from django.db import models

# Create your models here.
class Saccos(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    phone =  models.CharField(max_length=15, null=False)
    description = models.CharField(max_length=150, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=20, null=False)

    def __str__(self):
        return f'Sacco name: {self.name}'
    
class Vehicles(models.Model):
    licence_plate = models.CharField(max_length=10, null=False)
    sacco = models.ForeignKey(Saccos, on_delete=models.CASCADE)
    condition = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.licence_plate} Sacco: {self.sacco.name}'

class Destinations(models.Model):
    name = models.CharField(max_length=30, null=False)
    destination_id = models.CharField(max_length=10, null=False)
    sacco = models.ForeignKey(Saccos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} Sacco: {self.sacco.name}'
    
class Routes(models.Model):
    route = models.CharField(max_length=50, null=False)
    route_id = models.CharField(max_length=10, null=False)
    sacco = models.ForeignKey(Saccos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.route} Sacco: {self.sacco.name}'

class Drivers(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=False)
    phone = models.CharField(max_length=15, null=False)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    sacco = models.ForeignKey(Saccos, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return f'{self.full_name} Sacco: {self.sacco.name}'
    
class Conductors(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    surname = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=False)
    phone = models.CharField(max_length=15, null=False)
    vehicle = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    sacco = models.ForeignKey(Saccos, on_delete=models.CASCADE)

    @property
    def full_name(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return f'{self.full_name} Sacco: {self.sacco.name}'