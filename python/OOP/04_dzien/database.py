class Product (models.Model): 
    id = models.PrimaryKey(
        unique = True,
        autoincrement = True
    )
    category_id = models.ForeignKey(
        null = False
    )
    brand = models.ForeignKey(
        max_length = 30
    )
    name = models.CharField(
        max_length = 30
    )
    model = models.CharField(
        max_length = 30
    )
    stack = models.IntegerField(

    )
    availability_from = models.DateField(
        default = ''
    )
    picture = ImageField(
        max_size = 1024
    )
    short_description = models.TextField(
        max_length = 350
    )
    description = models.TextField(
        max_length = 5000
    )

class Category (models.Model):
    id = models.PrimaryKey(
        unique = True
    )
    brand = models.ForeignKey(
         max_length = 30
    )
    image = models.ImageField (
        max_size = 1024
    )
    link = models.URLField (

    )

    
