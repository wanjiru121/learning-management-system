from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    department_id = models.CharField(max_length=30)
    department_head = models.ForeignKey("trainer.Trainer",on_delete=models.CASCADE, related_name = "departments",null=True)

    class Meta:
        verbose_name_plural = "Departments"


    def __str__(self):
        return '{}'.format(self.name)