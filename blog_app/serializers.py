from rest_framework import serializers
from blog_app.models import Blog


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    author = serializers.CharField()
    description = serializers.CharField()
    post_date = serializers.DateField()
    is_public = serializers.BooleanField()
    slug = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Blog.objects.create(**validated_data)