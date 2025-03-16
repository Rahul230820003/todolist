from django.db import models


class Task(models.Model):
  title=models.CharField(max_length=200)
  completed=models.BooleanField(default=False)
  due_date=models.DateField(null=True,blank=True)
  created_at=models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.title
          
