from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
import logging
from apps.blog.models import Blog
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from apps.blog.serializers import CreateBlogSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_blog(request):
    try:
        logger.info("Received request to fetch blogs")
        # user = User.objects.get(id=request.user.id, is_active=True)
        blogs = Blog.objects.all()

        response_data = []
        for blog in blogs:
            blog_temp = {'id': blog.id, 'name': blog.name, 'description': blog.description}
            response_data.append(blog_temp)

        response = {'message': "All blogs fetched successfully", 'data': response_data}

        logger.info("Returning response with profile details")
        return Response(response, status=status.HTTP_200_OK)

    except Exception as error:
        logger.exception(error)
        response = {
            'message': "Blog does not exist"
        }
        return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_blog(request):
    try:
        logger.info("Receiver request to edit blog")
        request_data = request.data
        blog_data = request_data['blog']
        blog_id = blog_data['id']
        blog = Blog.objects.filter(id=blog_id).update(**blog_data)

        response = {
            "message": "Blog edited successfully"
        }
        return Response(response, status=status.HTTP_200_OK)

    except Exception as error:
        logger.exception(error)
        response = {
            'message': "Request data is not valid"
        }

    return Response(response, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    try:
        logger.info("Received request to create blog")
        request_data = request.data
        blog_data = request_data['blog']
        data = blog_data
        data['user'] = request.user

        # validate_data = CreateBlogSerializer(data=blog_data)

        blog = Blog.objects.create(**data)
        blog.save()

        response = {
            "message": "Blog created successfully"
        }
        return Response(response, status=status.HTTP_200_OK)

    except Exception as error:
        logger.exception(error)
        response = {
            'message': "Request data is not valid"
        }

        return Response(response, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blog(request, blog_id):
    try:
        logger.info("Received request to delete blog")
        Blog.objects.get(id=blog_id).delete()

        response = {
            "message": "Blog deleted successfully"
        }
        return Response(response, status=status.HTTP_200_OK)

    except Exception as error:
        logger.exception(error)
        response = {
            'message': "Blog does not exist"
        }
        return Response(response, status=status.HTTP_422_UNPROCESSABLE_ENTITY)



