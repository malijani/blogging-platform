from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    """ One To One relationship with User model """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        # Resize image when profile is saved
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)