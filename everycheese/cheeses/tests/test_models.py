import pytest

# Connects our tests with our database
pytestmark = pytest.mark.django_db

from ..models import Cheese


def test___str__():
    cheese = Cheese.objects.create(
        name="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
        firmness=Cheese.Firmness.SOFT,
    )
    assert cheese.__str__() == "Stracchino"
    assert str(cheese) == "Stracchino"