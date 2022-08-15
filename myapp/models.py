from django.db import models

# Create your models here.
class Details(models.Model):
    GENDER=[
                ('Male','Male'),
                ('Female','Female'),
                ('Others','Others')]
    QUALIFICATIONS=[
        ("No formal education","No formal education"),
        ("Primary education","Primary education"),
        ("Secondary education","Secondary education"),
        ("GED","GED"),
        ("Vocational qualification","Vocational qualification"),
        ("Bachelor's degree","Bachelor's degree"),
        ("Master's degree","Master's degree"),
        ("Doctorate or higher","Doctorate or higher")
    ]

    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10,choices=GENDER,default="Male")
    dob=models.DateField(null=True)
    qualification=models.CharField(max_length=30,choices=QUALIFICATIONS,default="No formal education")
    contact=models.PositiveIntegerField(default='0123456789')
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pictures/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,blank=True,null=True)

    def __str__(self):
        return f'{self.name}  :  {self.qualification}'


