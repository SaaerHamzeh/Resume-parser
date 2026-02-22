from .models import ResumeUpload
from rest_framework import serializers


class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = ["id", "file", "original_filename", "status", "uploaded_at"]
        read_only_fields = ["id", "original_filename", "status", "uploaded_at"]

    def create(self, validated_data):
        file = validated_data["file"]
        validated_data["original_filename"] = getattr(file, "name", "")
        return super().create(validated_data)
