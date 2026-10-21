class TaskDetail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OP=(
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
    )

    assigned_to=models.CharField(max_length=100)
    priority=models.CharField(
        max_length=1,choices=PRIORITY_OP,default=LOW)
