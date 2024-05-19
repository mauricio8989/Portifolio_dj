import pytest
from blog.factories import ProjectFactory

@pytest.fixture
def project():
    return ProjectFactory(title='Project Food Explorer')


@pytest.mark.django_db 
def test_created_project(project):
    assert project.title == 'Project Food Explorer'