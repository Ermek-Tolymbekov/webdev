from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import Company
from api.serializers import CompanySerializer, VacancySerializer


class CompanyListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)


class CompanyDetailAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            return Response({'message': str(e)})
        serializer = CompanySerializer(company)
        return Response(serializer.data)


class CompanyVacancyAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        try:
            company = Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            return Response({'message': str(e)})
        vacancies = company.vacancy_set.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
