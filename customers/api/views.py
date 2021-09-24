from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .serializers import UserSerializer, AddressSerializer


class CustomerSignUp(CreateAPIView):
    serializer_class = UserSerializer

# class Register(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = ''
#
#     def post(self, request, pk):
#         profile = get_object_or_404(UserSerializer)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'profile': profile})
#         serializer.save()
#         return redirect('profile-list')


class AddressInput(CreateAPIView):
    serializer_class = AddressSerializer
