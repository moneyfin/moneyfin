from rest_framework.views import APIView
from apps.user.models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from apps.user.serializers import CustomUserSerializer
from rest_framework import permissions
from rest_framework import authentication

class CustomUserListAPIViews(APIView):
    serializer_class = CustomUserSerializer
    
    def get_queryset(self):
        return CustomUser.objects.all()

    def get(self, request):
        serializer = self.serializer_class(
            self.get_queryset(),
            many=True
        )
        return Response(
            serializer.data,status=status.HTTP_200_OK
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
    

class CustomUserDetailAPIViews(APIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self, pk):
        return CustomUser.objects.get(id=pk)

    def get(self, request, pk):
        instance = self.get_queryset(pk)
        serializer = self.serializer_class(
            instance
        )
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):
        instance = self.get_queryset(pk)
        serializer = self.serializer_class(
            instance, 
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    
    def delete(self, request, pk):
        instance = self.get_queryset(pk)
        serializer = self.serializer_class(
            instance,
        )
        result = serializer.delete(instance)
        return Response(
            f"Detail: {result},\nResult: success",
            status=status.HTTP_204_NO_CONTENT
        )
