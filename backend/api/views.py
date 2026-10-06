from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import LabTest
from .serializers import LabTestSerializer
from .permissions import IsTechnician


class HealthCheckView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {
                "status": "ok",
                "service": "SecureLab API",
            }
        )


class LabTestListView(APIView):
    permission_classes = [IsAuthenticated, IsTechnician]

    def get(self, request):
        tests = LabTest.objects.filter(is_active=True)
        serializer = LabTestSerializer(tests, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = LabTestSerializer(data=request.data)

        if serializer.is_valid():
            test = serializer.save()

            return Response(
                LabTestSerializer(test).data,
                status=201,
            )

        return Response(
            serializer.errors,
            status=400,
        )