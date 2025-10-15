from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from rest_framework.permissions import AllowAny 
import jwt
from datetime import datetime, timedelta

class EmployeeLoginView(APIView):
    permission_classes = [AllowAny]
		
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        try:
            employee = Employee.objects.get(username=username)
        except Employee.DoesNotExist:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        if not employee.check_password(password):
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        payload = {
            "employee_id": employee.id,
            "exp": datetime.utcnow() + timedelta(hours=1),
            "iat": datetime.utcnow(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return Response({
            "access": token,
            "employee_id": employee.id,
            "employee_name": employee.name
        })

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
