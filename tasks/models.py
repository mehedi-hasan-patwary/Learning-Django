from django.db import models

# Create your models here.

class Employee(models.Model):
        name=models.CharField(max_length=100)
        email=models.EmailField(unique=True)

class Task(models.Model):
    assigned_to=models.ManyToManyField(Employee)
    project=models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        null=True)
        # default=1)
    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.DateField()
    is_completed=models.BooleanField(default=False)
    created=models.DateField(auto_now_add=True)  #jokhon create kore hoise tkn created er modhe time ta chole kabe
    updated_at=models.DateField(auto_now=True)
    #taskdetail_set auto ei name colomn create hoye gese


class TaskDetail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OP=(
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )

    task=models.OneToOneField(Task,on_delete=models.CASCADE,related_name="details")   
    assigned_to=models.CharField(max_length=100)
    priority=models.CharField(
        max_length=1,choices=PRIORITY_OP,default=LOW)



# from django.db import models

# # Create your models here.

# class Task(models.Model):
#     title=models.CharField(max_length=250)
#     description=models.TextField()
#     due_date=models.DateField()
#     is_completed=models.BooleanField(default=False)
#     created=models.DateField(auto_now_add=True)  #jokhon create kore hoise tkn created er modhe time ta chole kabe
#     updated_at=models.DateField(auto_now=True)


# class TaskDetail(models.Model):
#     HIGH='H'
#     MEDIUM='M'
#     LOW='L'
#     PRIORITY_OP=(
#         (HIGH,'High'),
#         (MEDIUM,'Medium'),
#         (LOW,'Low')
#     )

#     task=models.OneToOneField(Task,on_delete=models.CASCADE)   
#     assigned_to=models.CharField(max_length=100)
#     priority=models.CharField(
#         max_length=1,choices=PRIORITY_OP,default=LOW)

class Project(models.Model):
    name=models.CharField(max_length=100)
    start_date=models.DateField()






