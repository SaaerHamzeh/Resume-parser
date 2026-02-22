from django.db import models


# Create your models here.
class ResumeUpload(models.Model):
    STATUS_CHOICES = (
        ("UPLOADED", "UPLOADED"),
        ("PARSED", "PARSED"),
        ("FAILED", "FAILED"),
    )

    file = models.FileField(upload_to="resumes/")
    original_filename = models.CharField(max_length=250, blank=True, null=True)
    parsed_data = models.JSONField(blank=True, null=True)
    status = models.CharField(
        max_length=250, choices=STATUS_CHOICES, default="UPLOADED"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.original_filename} - {self.status}"
