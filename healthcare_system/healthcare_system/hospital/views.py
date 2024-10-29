from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PatientSignupSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PatientLoginSerializer

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
