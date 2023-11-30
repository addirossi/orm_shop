from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)


class Car(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=20)
    volume = models.DecimalField(max_digits=2, decimal_places=1)
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'


class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='purchases')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='sales')
    created_at = models.DateTimeField(auto_now_add=True)
