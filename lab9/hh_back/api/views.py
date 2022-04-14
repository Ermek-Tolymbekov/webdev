from django.http.response import JsonResponse

from api.models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies = [company.to_json() for company in companies]
    return JsonResponse(companies, safe=False)


def get_company(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(company.to_json())


def company_vacancy(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    vacancies = company.vacancy_set.all()
    vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies, safe=False)


def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies, safe=False)


def get_vacancy(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    return JsonResponse(vacancy.to_json())


def top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies, safe=False)
