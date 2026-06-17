from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Certificate, ContactMessage, Experience, Profile, Project, Resume, Skill
from .serializers import (
    CertificateSerializer,
    ContactMessageSerializer,
    ExperienceSerializer,
    ProjectSerializer,
    SkillSerializer,
)


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class HomeView(APIView):
    """Root endpoint with links to admin and API."""

    def get(self, request):
        return Response({
            'message': 'Portfolio API is running.',
            'frontend': 'http://localhost:5173/',
            'admin': request.build_absolute_uri('/admin/'),
            'endpoints': {
                'portfolio': request.build_absolute_uri('/api/portfolio/'),
                'skills': request.build_absolute_uri('/api/skills/'),
                'certificates': request.build_absolute_uri('/api/certificates/'),
                'projects': request.build_absolute_uri('/api/projects/'),
                'experience': request.build_absolute_uri('/api/experience/'),
                'contact': request.build_absolute_uri('/api/contact/'),
            },
        })


def _get_profile_image_url(request):
    profile = Profile.objects.first()
    if profile and profile.profile_image:
        return request.build_absolute_uri(profile.profile_image.url)
    return None


def _get_active_cv_url(request):
    resume = Resume.objects.filter(is_active=True).first()
    if resume and resume.file:
        return request.build_absolute_uri(resume.file.url)
    return '#'


class PortfolioDataView(APIView):
    """Single endpoint returning all portfolio data."""

    def get(self, request):
        return Response({
            'profile': {
                'name': 'Shivam Verma',
                'title': 'IOT ENGINEER | SOFTWARE DEVELOPER',
                'tagline': 'Passionate Learner | Creative Thinker',
               'bio': (
    "I'm Shivam Verma, a B.Voc (Internet of Things) student at Dayalbagh "
    "Educational Institute and an aspiring IoT Engineer & Software Developer. "
    "I have experience in developing IoT-based solutions, web applications, "
    "and automation projects using Python, Django, React, JavaScript, MySQL, "
    "Arduino, and ESP32. I enjoy learning new technologies, solving real-world "
    "problems, and building innovative solutions that combine hardware and "
    "software to create meaningful impact."
),
                'roles': [
                         'IoT Engineer',
                         'Software Developer',
                         'Django Developer',
                         'Problem Solver',         
                 ],
                'cv_url': _get_active_cv_url(request),
                'social': {
                    'github': 'https://github.com/shivam00-web',
                    'linkedin': 'https://www.linkedin.com/in/shivam9528/',
                    'email': 'sv873234@gmail.com',
                },
                'profile_image': _get_profile_image_url(request),
            },
            'skills': SkillSerializer(
                Skill.objects.all(), many=True, context={'request': request},
            ).data,
            'certificates': CertificateSerializer(
                Certificate.objects.all(), many=True, context={'request': request},
            ).data,
            'experience': ExperienceSerializer(Experience.objects.all(), many=True).data,
            'projects': ProjectSerializer(Project.objects.all(), many=True).data,
        })
