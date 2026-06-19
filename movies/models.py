from django.db import models

class Mahsulot(models.Model):
    # 1. Main Information
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.CharField(max_length=400)  
    duration = models.CharField(max_length=50)  # e.g., "2h 30m"
    video = models.CharField(max_length=500)  # Link to the movie video
    image = models.CharField(max_length=500, blank=True, null=True)  # Link to the movie poster
        
    
    # 2. Categorization & Rating
    genre = models.CharField(max_length=100)       # e.g., "Action", "Comedy"
    rating = models.CharField(max_length=20)         # e.g., "IMDb 7.5"
    
    # 3. People involved
    company = models.CharField(max_length=255)     # e.g., "Warner Bros."
    cast = models.TextField()                       # List of main actors
    