from rest_framework import serializers
from api.models import Vacancy, Company


class VacancySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    def create(self, validated_data):
        vacancy = Vacancy.objects.create(name=validated_data.get('name'),
                                         description=validated_data.get('description'),
                                         salary=validated_data.get('salary'),
                                         company=validated_data.get('company'))
        return vacancy

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.salary = validated_data.get('salary')
        instance.company = validated_data.get('company')
        instance.save()
        return instance


class CompanySerializer(serializers.ModelSerializer):
    vacancies = VacancySerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancies')

