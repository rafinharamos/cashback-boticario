import requests
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from cashback import settings

from sales.api.v1.serializers import CreateSalesSerializer, ListSalesSerializer
from sales.models import Sale


class CreateSalesView(APIView):
    """ Create a new sales instance """

    serializer_class = CreateSalesSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CreateSalesSerializer(data=request.data or None)
        if serializer.is_valid():
            serializer.save(salesman_id=self.request.user.id)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListSalesView(ListAPIView):
    """Return informations of sales of an user """

    permission_classes = (IsAuthenticated,)
    serializer_class = ListSalesSerializer

    def get_queryset(self):
        queryset = Sale.objects.filter(salesman_id=self.request.user.id)
        return queryset


class ListAccumulatedCashback(APIView):
    """Return accumulated  cashback of an user """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        url = settings.API_TOTAL_CASHBACK + self.request.user.cpf
        try:
            response = requests.get(url)
            return Response(response.json())
        except:
            return Response(
                {"system unavaible at the moment"}, status=status.HTTP_400_BAD_REQUEST
            )
