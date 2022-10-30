from rest_framework import serializers
from apps.blog.models import Blog


class CreateBlogSerializer(serializers.Serializer):
    """
        Serializer to validate blog data
    """

    name = serializers.CharField(max_length=250, required=True)

    class Meta:
        model = Blog
        fields = ['name', 'description']
