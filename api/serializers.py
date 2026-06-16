from rest_framework import serializers

from .models import Certificate, ContactMessage, Experience, Project, Skill


def _absolute_file_url(request, file_field):
    if file_field and request:
        return request.build_absolute_uri(file_field.url)
    return None


class DisplayImageSerializerMixin:
    def get_image(self, obj):
        return _absolute_file_url(self.context.get('request'), obj.image)

    def get_image_url(self, obj):
        return obj.image_url or None

    def get_display_image(self, obj):
        uploaded = self.get_image(obj)
        if uploaded:
            return uploaded
        if obj.image_url:
            return obj.image_url
        return None


class SkillSerializer(DisplayImageSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ['id', 'title', 'description', 'image', 'image_url', 'display_image', 'order']


class CertificateSerializer(DisplayImageSerializerMixin, serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    display_image = serializers.SerializerMethodField()

    class Meta:
        model = Certificate
        fields = [
            'id', 'title', 'description', 'image', 'image_url',
            'display_image', 'download_url', 'order',
        ]


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'id', 'role', 'company', 'location', 'start_date',
            'end_date', 'is_current', 'description', 'order',
        ]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'image_url',
            'project_url', 'github_url', 'status', 'order',
        ]


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_at']
        read_only_fields = ['id', 'created_at']
