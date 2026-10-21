from django.db import models

# Create your models here.

class Task(models.Model):
    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateField()
    is_completed=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)  #jokhon create kore hoise tkn created er modhe time ta chole kabe
    updated_at=models.DateField(auto_now=True)


class TaskDetail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OP=(
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )

    task=models.OneToOneField(Task,on_delete=models.CASCADE)   
    assigned_to=models.CharField(max_length=100)
    priority=models.CharField(
        max_length=1,choices=PRIORITY_OP,default=LOW)



