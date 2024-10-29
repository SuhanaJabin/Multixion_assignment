from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PatientSignupSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PatientLoginSerializer
from rest_framework import generics
from .models import Patient
from .serializers import PatientDetailSerializer
from django.utils.translation import gettext as _

class PatientSignupView(APIView):
    def post(self, request):
        serializer = PatientSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class PatientLoginView(APIView):
    def post(self, request):
        serializer = PatientLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Here, you can implement any session handling or token generation.
            return Response({
                "message": "Login successful",
                "user_id": user.id
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()  # Get all patients
    serializer_class = PatientDetailSerializer