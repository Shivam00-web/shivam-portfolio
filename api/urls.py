from django.urls import path

from .views import (
    CertificateListView,
    ContactCreateView,
    ExperienceListView,
    PortfolioDataView,
    ProjectListView,
    SkillListView,
)

urlpatterns = [
    path('portfolio/', PortfolioDataView.as_view(), name='portfolio-data'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('certificates/', CertificateListView.as_view(), name='certificate-list'),
    path('experience/', ExperienceListView.as_view(), name='experience-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
]
