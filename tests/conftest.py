import pytest
import copy
import json
from backend import app, routes

@pytest.fixture()
def client():
    """Each test starts with the same ten seed pictures, independent of order."""
    routes.data[:] = copy.deepcopy(json.loads(routes._data_file.read_text(encoding='utf-8')))
    app.config.update(TESTING=True)
    return app.test_client()

@pytest.fixture()
def picture():
    return {'id':200,'pic_url':'https://example.org/test.jpg','event_country':'United States',
            'event_state':'California','event_city':'Fremont','event_date':'11/2/2030'}
