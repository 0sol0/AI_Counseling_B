from rest_framework import serializers
from articles.models import Article

class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    class Meta:
        model = Article
        fields = ('user', 'title', 'content', 'created_at')
        