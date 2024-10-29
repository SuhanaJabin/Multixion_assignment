# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminUser, IsDoctorOrNurse

# Example view restricted to Admin users
class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

# Example view restricted to Doctors and Nurses
class DoctorOrNurseView(APIView):
    permission_classes = [IsDoctorOrNurse]

    def get(self, request):
        return Response({"message": "Hello, Doctor or Nurse!"})


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .permissions import IsAdminUser, IsDoctorOrNurse

class CheckPermissionView(APIView):
    """
    API endpoint to check if the current user has the required role permissions.
    """
    permission_classes = [IsAuthenticated]  # Ensure user is logged in first

    def get(self, request):
        user_role = request.user.role

        # Check Admin Permissions
        if IsAdminUser().has_permission(request, self):
            return Response({"message": "User has admin permissions"}, status=status.HTTP_200_OK)

        # Check Doctor or Nurse Permissions
        elif IsDoctorOrNurse().has_permission(request, self):
            return Response({"message": f"User has {user_role} permissions"}, status=status.HTTP_200_OK)

        # If no matching permissions, user is unauthorized for specific actions
        return Response({"message": "User does not have the required permissions"}, status=status.HTTP_403_FORBIDDEN)
