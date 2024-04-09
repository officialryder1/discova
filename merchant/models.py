from django.db import models
from django.contrib.auth.models import User

class Merchant(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='merchant_img')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.IntegerField()
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)


class MessageAdmin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    detail = models.CharField(max_length=50)
    message = models.TextField()
    image = models.ImageField(upload_to='M2A_message', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail + " - " + " Message Sent By " + str(self.user)
    

class Reply(models.Model):
    user = models.ForeignKey(MessageAdmin, on_delete=models.CASCADE)
    message = models.TextField()
    image = models.ImageField(upload_to='M2A_message', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "You Replied " + str(self.user)
    
