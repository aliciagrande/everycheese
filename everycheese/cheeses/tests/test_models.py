import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese
from .factories import CheeseFactory

#     cheese = Cheese.objects.create(
#         name="Stracchino",
#         description="Semi-sweet cheese that goes well with starches.",
#         firmness=Cheese.Firmness.SOFT,
#     )

def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name

def test_get_absolute_url():
    cheese = CheeseFactory()
    url = cheese.get_absolute_url()
    assert url == f'/cheeses/{cheese.slug}/'