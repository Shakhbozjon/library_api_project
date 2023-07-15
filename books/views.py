from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer

from rest_framework import generics, status


# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f"Returned {len(books)} books",
            'books': serializer_data

        }
        return Response(data)





# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data

            data = {
                'status': 'Successful',
                'book': serializer_data
            }

            return Response(data, status.HTTP_200_OK)

        except Exception:
            return Response({
                'status': 'False',
                'message': 'Book is not found'
            }, status=status.HTTP_404_NOT_FOUND
            )







# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
        def delete(self, request, pk):
            try:
                book = Book.objects.get(id=pk)
                book.delete()
                return Response(
                    {
                        'status': True,
                        'message': 'Successfully deleted '
                    },
                    status.HTTP_200_OK
                )
            except Exception:
                return Response(
                    {
                        'status': False,
                        'Message': 'Book is not found'
                    },
                    status.HTTP_400_BAD_REQUEST
                )



# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response(
                {
                    'status': True,
                    'message': f"book {book_saved} updated successfully"
                }
            )





# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            data = {
                    'status': f'Books are saved to the database',
                    'books': data
                   }

            return Response(data)

        else:
            return Response(
                {
                    'status': False,
                    'message': 'Serializer is not valid'
                },
                status=status.HTTP_400_BAD_REQUEST
            )








class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer