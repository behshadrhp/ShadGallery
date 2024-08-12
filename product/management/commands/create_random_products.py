import random

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from io import BytesIO
from PIL import Image

from product.models import Product


class Command(BaseCommand):
    help = "Generate random products with random images and colors"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int, help="ID of the user to assign the products to")
        parser.add_argument("count", type=int, help="Number of random products to create")

    def handle(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        count = kwargs["count"]

        from django.contrib.auth import get_user_model
        User = get_user_model()
        user = User.objects.get(id=user_id)

        for _ in range(count):
            color = self.get_random_color()
            self.save_image_to_product(user, color)

        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} random products."))

    def generate_random_image(self, color):
        # Create a 100x100 image with the given color

        image = Image.new("RGB", (100, 100), color)
        return image

    def get_random_color(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
        return random.choice(colors)

    def save_image_to_product(self, user, color):
        image = self.generate_random_image(color)
        
        # Save image to a BytesIO object
        img_io = BytesIO()
        image.save(img_io, format="JPEG")
        img_io.seek(0)
        
        # Create a new Product instance
        product = Product(user=user, title=f"Product with {color} color", description=f"This is a {color} product.")
        
        # Save the image to the ImageField
        product.image.save(f"{color}_image.jpg", ContentFile(img_io.read()), save=False)
        
        # Save the Product instance to the database
        product.save()

        # Add random tags
        product.tag.add("Random", color)
        
        # Save the Product instance again to ensure tags are saved
        product.save()
