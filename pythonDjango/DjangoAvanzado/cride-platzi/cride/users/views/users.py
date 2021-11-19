"""Users views."""

# Django Rest Framwork
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializer
from cride.serializers.users import UserLoginSerializer

class UserLoginAPIView(APIView):
    """Users login APIView."""

    def post(self, request, *args,  **Kwargs):
        """Handle HTTP post request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        data = {
            'status': 'ok',
            'token': token
        }

        return Response(data, status = status.HTTP_201_CREATED)