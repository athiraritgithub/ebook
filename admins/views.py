
from rest_framework.views import APIView
from admins.models import Ebooks
from rest_framework.response import Response
from admins.serializers import BookSerializers,UserSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate,login
from rest_framework import permissions,authentication

class Ebookview(APIView):

    # permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]
    def get(self,request,*args,**kwargs):
        all_books=Ebooks.objects.all().order_by('-id')
        allbook_serializer=BookSerializers(all_books,many=True)
        return Response(allbook_serializer.data)


    def post(self,request,*args,**kwargs):
        allbook_serializer=BookSerializers(data=request.data)
        if allbook_serializer.is_valid():
            allbook_serializer.save()
            return Response(allbook_serializer.data)


class EbookDetails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id=kwargs.get("ebook_id")
        book=Ebooks.objects.get(id=id)
        book_serializer=BookSerializers(book)
        return Response(book_serializer.data)

    authentication_classes = [authentication.TokenAuthentication]
    def put(self,request,*args,**kwargs):
        id=kwargs.get("ebook_id")
        book=Ebooks.objects.get(id=id)
        book_serilizer=BookSerializers(instance=book,data=request.data)
        if book_serilizer.is_valid():
            book_serilizer.save()
            return Response(book_serilizer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("ebook_id")
        book=Ebooks.objects.get(id=id)
        book.delete()
        return Response({"msg":"deleted"})

class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):
        usr_ser=UserSerializer(data=request.data)
        if usr_ser.is_valid():
            usr_ser.save()
            return Response({"msg":"registration successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response(usr_ser.errors,status=status.HTTP_400_BAD_REQUEST)


class SignInView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            uname=serializer.validated_data.get("username")
            password=serializer.validated_data.get("password")
            user=authenticate(request,username=uname,password=password)
            if user:
                login(request,user)
                return Response({"msg":"success"})
            else:
                return Response({"msg":"invalid credentials"})