from django.db import models


class Message(models.Model):
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.timestamp}"
    
class MessagePerson(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __str__(self):
        return f"Hello {self.name} {self.lastname}"
    

