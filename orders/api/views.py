from rest_framework.generics import CreateAPIView
from .serializers import DiscountSerializer

class DiscountView(CreateAPIView):
    serializer_class = DiscountSerializer

