from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Portfoliocategory(models.Model):
    projectCategory = models.CharField(max_length=200)

    def __str__(self):
        return self.projectCategory



class Portfolio(models.Model):
    project_name = models.CharField(max_length = 200)
    client = models.CharField(max_length=50, null= True)
    # active = models.BooleanField(default=False)
    category = models.ForeignKey(Portfoliocategory, on_delete = models.CASCADE, null=True)
    description = models.TextField(max_length=300, null= True)
    project_url = models.URLField(max_length = 50, null=True)
    image = models.ImageField(null=True, blank=True, upload_to = 'img')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.project_name

    @property
    def my_image(self):

        if self.image :
            return self.image.url
        return ''
    
class Resume_details(models.Model):
    summary = models.TextField(max_length= 500, null= True)
    state = models.CharField(max_length = 100, null= True)
    phone = models.CharField(max_length= 100, null=True)
    email = models.CharField(max_length= 50, null= True)
    education_title = models.CharField(max_length=100, null=True)
    education_date = models.CharField(max_length = 20, null=True)
    education_name = models.CharField(max_length = 200, null= True)

    def __str__(self):
        return self.email

class Resume_responsibility(models.Model):
    responsibility = models.CharField(null= True, max_length= 200)

    def __str__(self):
        return self.responsibility
    

class Resume(models.Model):  
    role = models.CharField(max_length= 50)
    date = models.CharField(max_length=20, null=True)
    company_name = models.CharField(max_length=100, null=True)
    response = models.ManyToManyField(Resume_responsibility)
    created = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.role

    class Meta:
        ordering = ['-created']


    
class Rate(models.Model):
    name = models.CharField(max_length=30, null= True)
    review = models.TextField(max_length=500, null=True)
    image = models.ImageField(null=True, blank=True, default='../static/assets/img/avatar/avatar.svg')
    occupation = models.CharField(null=True, blank=False, max_length=200, default= '')
    approve = models.BooleanField(default=False)
    created = models.TimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']
    @property
    def rate_image(self):
        if self.image :
            return self.image.url
        return ''
    
    def approve_ref(self):
        self.approve = True
        self.save()

    def __str__(self):
        return self.name

class About(models.Model):
    description1 = models.TextField(max_length= 500, null= True)
    birthday = models.CharField(max_length= 50, null= True)
    phone = models.CharField(max_length= 50, null= True)
    city = models.CharField(max_length= 50, null= True)
    Degree = models.CharField(max_length= 50, null=True)
    email = models.CharField(max_length=50, null= True)
    freelance = models.CharField(max_length= 50, null=True)
    description2 = models.TextField(max_length= 500, null=True)

    def __str__(self):
        return self.description1

class Skills(models.Model):
    skill = models.CharField(max_length= 50, null= True)
    level = models.CharField(max_length= 50, null=True)
    aria_level = models.CharField(max_length= 50, null= True)

    def __str__(self):
        return self.skill


