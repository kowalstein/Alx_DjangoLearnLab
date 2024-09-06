from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):

    """
    Serializer for Book model.
    This handles the serialization of Book instances.
    It includes custom validation to ensure the publication year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        This validates that the publication year is not in the future
        """
        if value > 2024:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    This includes a nested BookSerializer to serialize related books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
