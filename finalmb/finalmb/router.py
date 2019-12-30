from students.api.viewsets import StudentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentViewSet)