from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView

from .models import ResumeUpload
from .serializers import ResumeUploadSerializer
from .services.extractor import extract_text_from_pdf
from .services.llm_parser import parse_resume_with_llm


class ResumeUploadView(CreateAPIView):
    serializer_class = ResumeUploadSerializer
    parser_classes = (MultiPartParser, FormParser)


class ResumeParseView(APIView):

    def post(self, request, pk):
        try:
            resume = ResumeUpload.objects.get(pk=pk)
        except ResumeUpload.DoesNotExist:
            return Response({"error": "Not found"}, status=404)

        try:
            text = extract_text_from_pdf(resume.file.path)
            parsed = parse_resume_with_llm(text)

            resume.parsed_data = parsed.dict()
            resume.status = "PARSED"
            resume.save()

            return Response(resume.parsed_data)

        except Exception as e:
            resume.status = "FAILED"
            resume.save()
            return Response({"error": str(e)}, status=500)
