from django.db import models
from django.contrib.auth.models import User
from django.db import connections
from datetime import datetime
# Create your models here.





class registration(models.Model):
    UserName=models.CharField(max_length=100,null=True)
    FirstName=models.CharField(max_length=100,null=True)
    LastName=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,unique=True,primary_key=True)
    Password=models.CharField(max_length=300,null=True)
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    

    def __str__(self):
        return f'{self.Email}'


    # class Meta:
    #     db_table="registration"

class Post(models.Model):
    Title=models.CharField(max_length=100,null=True)
    Overview=models.CharField(max_length=1000,null=True)
    Time_upload=models.DateTimeField(default=datetime.now,blank=True)
    Author=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Category=models.CharField(max_length=100,null=True)
    Thumbnail=models.ImageField(null=True,blank=True,upload_to='media/')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    class Meta:
        # db_table="post"
        ordering = ['-Time_upload',]

    def delete(self, *args):
        self.Thumbnail.delete()
        super().delete(*args)




class Preference(models.Model):
    user= models.ForeignKey(registration,on_delete=models.CASCADE,null=True)
    post= models.ForeignKey(Post,on_delete=models.CASCADE,null=True)
    value= models.IntegerField(null=True)
    
    
    def __str__(self):
        return str(self.user) + ':' + str(self.post) +':' + str(self.value)

    class Meta:
        unique_together = ("user", "post", "value")
        # db_table="preference"


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
    time=models.DateTimeField(default=datetime.now,blank=True)
    comm=models.TextField()
    im=models.ImageField(null=True,blank=True)


    # class Meta:
    #     db_table="comment"





class Subcomment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
    time=models.DateTimeField(default=datetime.now,blank=True)
    comm=models.TextField()
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    ima=models.ImageField(null=True,blank=True)


    # class Meta:
    #     db_table="subcomment"


