from models.metrics_model import MetricsModel

def test_metrics_model_initialization():
    model = MetricsModel(10, 5, 20, 0.75)
    assert model.total_likes == 10
    assert model.total_dislikes == 5
    assert model.total_messages == 20
    assert model.positive_rating == 0.75

def test_get_total_likes():
    model = MetricsModel(10, 5, 20, 0.75)
    assert model.get_total_likes() == 10

def test_get_total_dislikes():
    model = MetricsModel(10, 5, 20, 0.75)
    assert model.get_total_dislikes() == 5

def test_get_total_messages():
    model = MetricsModel(10, 5, 20, 0.75)
    assert model.get_total_messages() == 20

def test_get_positive_rating():
    model = MetricsModel(10, 5, 20, 0.75)
    assert model.get_positive_rating() == 0.75