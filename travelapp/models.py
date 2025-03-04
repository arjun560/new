from django.db import models

# Create your models here.
 
class Test(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    review = models.TextField()
    def __str__(self):
        return self.name
    
class TourPreference(models.Model):
    TOUR_TYPES = [
        ('Romantic', 'Romantic'),
        ('Solo', 'Solo'),
        ('Family', 'Family'),
        ('Friends', 'Friends'),
        ('Business Trip', 'Business Trip'),
        ('Honeymoon', 'Honeymoon'),
        ('Adventure', 'Adventure'),
    ]
    ACCOMMODATION_TYPES = [
        ('Hotel', 'Hotel'),
        ('Resort', 'Resort'),
        ('Apartment', 'Apartment'),
        ('Campsite', 'Campsite'),
        ('Guesthouse', 'Guesthouse'),
    ]

    tour_type = models.CharField(max_length=50, choices=TOUR_TYPES)
    budget = models.PositiveIntegerField()
    num_days = models.PositiveIntegerField()
    destination = models.CharField(max_length=100)
    starting_location = models.CharField(max_length=100)
    accommodation_type = models.CharField(max_length=50, choices=ACCOMMODATION_TYPES)
    interest = models.CharField(max_length=200, blank=True, null=True)
    distance_range = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.tour_type} to {self.destination}"
class Destination(models.Model):
    TOUR_TYPES = [
        ('Romantic', 'Romantic'),
        ('Solo', 'Solo'),
        ('Family', 'Family'),
        ('Friends', 'Friends'),
        ('Business Trip', 'Business Trip'),
        ('Honeymoon', 'Honeymoon'),
        ('Adventure', 'Adventure'),
    ]
    ACCOMMODATION_TYPES = [
        ('Hotel', 'Hotel'),
        ('Resort', 'Resort'),
        ('Apartment', 'Apartment'),
        ('Campsite', 'Campsite'),
        ('Guesthouse', 'Guesthouse'),
    ]

class Destination(models.Model):
    TOUR_TYPES = [
        ('Romantic', 'Romantic'),
        ('Solo', 'Solo'),
        ('Family', 'Family'),
        ('Friends', 'Friends'),
        ('Business Trip', 'Business Trip'),
        ('Honeymoon', 'Honeymoon'),
        ('Adventure', 'Adventure'),
    ]
    ACCOMMODATION_TYPES = [
        ('Hotel', 'Hotel'),
        ('Resort', 'Resort'),
        ('Apartment', 'Apartment'),
        ('Campsite', 'Campsite'),
        ('Guesthouse', 'Guesthouse'),
    ]

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    tour_type = models.CharField(max_length=50, choices=TOUR_TYPES)
    accommodation_type = models.CharField(max_length=50, choices=ACCOMMODATION_TYPES)
    interest = models.CharField(max_length=200, blank=True, null=True)
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
