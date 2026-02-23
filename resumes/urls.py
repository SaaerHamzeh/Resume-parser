from django.urls import path
from .views import ResumeUploadView, ResumeParseView, ResumeListView

urlpatterns = [
    path("resumes/", ResumeListView.as_view(), name="resume-list"),
    path("resumes/upload/", ResumeUploadView.as_view(), name="resume-upload"),
    path("resumes/<int:pk>/parse/", ResumeParseView.as_view(), name="resume-parse"),
]
