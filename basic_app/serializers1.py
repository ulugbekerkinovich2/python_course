from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from basic_app import models
from basic_app.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'content', 'price', 'isbn')

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            print('ss')
            raise ValidationError({
                'status': False,
                "message": 'kitobni sarlavhasi harflardan tashkil topgan bolishi kerak'
            })
        if Book.objects.filter(title=title).exists:
            raise ValidationError({
                'status': 'bunday title mavjud'
            })

        if author.isdigit():
            raise ValidationError({
                "status": 'author raqamlardan tashkil topmasligi kerak'
            })

    def validate_isbn(self, isbn):
        if '4' in isbn:
            raise ValidationError({
                'message': 'isbn 4 ,raqamidan foydalanilmasligi kerak'
            })
