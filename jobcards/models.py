from django.db import models
import uuid


class JobCard(models.Model):
    # Auto-generated Job Card Number
    job_card_no = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    # Client Details
    full_name = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()

    # Vehicle Details
    vehicle_make_model = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    registration_number = models.CharField(max_length=50)
    mileage = models.PositiveIntegerField()
    vin_chassis_number = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    # Service Details
    service_description = models.TextField()
    serviced_recently = models.BooleanField(default=False)
    preferred_service_date = models.DateField()
    additional_concerns = models.TextField(blank=True, null=True)

    # Confirmation
    confirmation = models.BooleanField(default=False)

    # Payment & Status (future scalability)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('paid', 'Paid'),
            ('failed', 'Failed'),
        ],
        default='pending'
    )
    
    payment_reference = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    STATUS_CHOICES = [
        ('new', 'New'),
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    def save(self, *args, **kwargs):
        if not self.job_card_no:
            self.job_card_no = self.generate_job_card_no()
        super().save(*args, **kwargs)

    def generate_job_card_no(self):
        return f"KNUST-JC-{uuid.uuid4().hex[:8].upper()}"

    def __str__(self):
        return f"{self.job_card_no} - {self.full_name}"
