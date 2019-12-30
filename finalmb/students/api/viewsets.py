from students.models import basic_info, mapr
from .serializers import StudentSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
	queryset = basic_info.objects.all()
	serializer_class = StudentSerializer

	