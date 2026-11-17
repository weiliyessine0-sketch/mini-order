import pytest
from app.web import create_app
from app.order_service import OrderService

@pytest.fixture()
def client():
    service = OrderService()
    app = create_app(service)
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client
