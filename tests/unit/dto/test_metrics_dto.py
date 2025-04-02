from dto.metrics_dto import MetricsDTO

def test_metrics_dto_initialization():
    metrics = MetricsDTO(
        total_likes=100,
        total_dislikes=20,
        total_messages=50,
        positive_rating=80.0
    )
    assert metrics.get_total_likes() == 100
    assert metrics.get_total_dislikes() == 20
    assert metrics.get_total_messages() == 50
    assert metrics.get_positive_rating() == 80.0

def test_metrics_dto_default_initialization():
    metrics = MetricsDTO(0, 0, 0, 0.0)
    assert metrics.get_total_likes() == 0
    assert metrics.get_total_dislikes() == 0
    assert metrics.get_total_messages() == 0
    assert metrics.get_positive_rating() == 0.0