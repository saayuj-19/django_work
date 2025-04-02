

from django.db import models

class Costumer(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.account_number})"

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True, default=1001)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"

class Bill(models.Model):
    BILL_STATUS_CHOICES = (
        ('P', 'Paid'),
        ('U', 'Pending'),
    )

    costumer = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    bill_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=2, choices=BILL_STATUS_CHOICES, default='U')
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.remaining_balance = self.total_amount - self.amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill for {self.costumer.first_name} {self.costumer.last_name} - {self.total_amount} ({self.status})"
    
    class Meta:
        unique_together = ('costumer', 'bill_date')


