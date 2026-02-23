from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

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


class ResumeListView(APIView):

    def get(self, request):

        queryset = ResumeUpload.objects.all()

        # 🔍 Search by name or email inside JSONField
        search = request.query_params.get("search")
        if search:
            queryset = queryset.filter(
                Q(parsed_data__name__icontains=search)
                | Q(parsed_data__email__icontains=search)
            )

        # 📅 Filter by status
        status_param = request.query_params.get("status")
        if status_param:
            queryset = queryset.filter(status=status_param)

        # 📆 Filter by date range
        uploaded_after = request.query_params.get("uploaded_after")
        uploaded_before = request.query_params.get("uploaded_before")

        if uploaded_after:
            queryset = queryset.filter(uploaded_at__gte=uploaded_after)

        if uploaded_before:
            queryset = queryset.filter(uploaded_at__lte=uploaded_before)

        # 🔀 Ordering
        ordering = request.query_params.get("ordering", "-uploaded_at")
        queryset = queryset.order_by(ordering)

        # 📄 Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10

        result_page = paginator.paginate_queryset(queryset, request)
        serializer = ResumeUploadSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
