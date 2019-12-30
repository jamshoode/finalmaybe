from rest_framework import serializers
from students.models import basic_info, mapr

class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = basic_info
		fields = ('first_name', 'last_name')

	class Meta:
		model = mapr
		fields = ('marks', 'presence')

