import pytest
from django.urls import reverse, resolve
from .factories import CheeseFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def cheese():
    return CheeseFactory()


def test_list_reverse():
    """cheeses:list should reverse to /cheeses/."""
    assert reverse('cheeses:list') == '/cheeses/'

def test_list_resolve():
    """/cheeses/ should resolve to cheeses:list."""
    assert resolve('/cheeses/').view_name == 'cheeses:list'


def test_detail_reverse(cheese):
    """cheeses:detail should reverse to /cheeses/cheeseslug/."""
    url = reverse('cheeses:detail',
         kwargs={'slug': cheese.slug})
    assert url == f'/cheeses/{cheese.slug}/'

def test_detail_resolve(cheese):
    """/cheeses/cheeseslug/ should resolve to cheeses:detail."""
    url = f'/cheeses/{cheese.slug}/'
    assert resolve(url).view_name == 'cheeses:detail'

