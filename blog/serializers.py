from rest_framework import serializers
from .models import Post

# serializers here
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created',) # OR '__all__'
        model = Post
