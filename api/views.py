from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):

    def get(self, request):
        data = {'message': 'Access Granted!', 'user': request.user.username }
        return Response(data, status=status.HTTP_200_OK)
