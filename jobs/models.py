from django.db import models

# Create your models here.
class Job(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    min_offer = models.DecimalField(max_digits=10, decimal_places=2)
    max_offer = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.job_title

class JobApplicant(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('applied', 'Applied'), ('interviewing', 'Interviewing'), ('offered', 'Offered'), ('rejected', 'Rejected')], default='applied')

    def __str__(self):
        return f"{self.user.username} - {self.job.job_title}"