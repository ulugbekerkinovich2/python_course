from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book
import json
from decimal import Decimal


# class DecimalEncoder(json.JSONEncoder):
#     def default(self, o):
#         if isinstance(o, Decimal):
#             return str(o)
#         return super().default(o)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError({
                'status': False,
                "message": 'kitobni sarlavhasi harflardan tashkil topgan bolishi kerak'
            })
        # if Book.objects.filter(title=title, author=author).exists():
        #     raise ValidationError(
        #         {
        #             'status': False,
        #             "message": 'kitobni sarlavhasi bir xil bolmasligi kerak'
        #         }
        #     )
        return data

    # def validate_isbn(self, isbn):
    #     if int(isbn) < 0 or int(isbn) > 99999997777:
    #         raise ValidationError(
    #             {
    #                 'status': False,
    #                 "message": 'isbn juda katta'
    #             }
    #         )


class BookDetailApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price')
