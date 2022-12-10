from django.db import models


class Card(models.Model):
    """Loyalty card."""
    STATUS_CHOICES = [
        ('NO', 'Not activated'),
        ('AC', 'Activated'),
        ('EX', 'Expired'),
    ]
    series = models.CharField(max_length=3)
    number = models.IntegerField(unique=True)
    release_date = models.DateTimeField(auto_now_add=True)
    use_date = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='NO')

    class Meta:
        ordering = ('-expiration_date',)

    def __str__(self) -> str:
        return f'{self.series}{self.number}'
