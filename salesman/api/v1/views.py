from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from salesman.api.v1.serializers import CreateSalesmanSerializer


class CreateSalesmanView(APIView):
    """ Create a new salesman instance """

    serializer_class = CreateSalesmanSerializer

    def post(self, request):
        serializer = CreateSalesmanSerializer(data=request.data or None)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
