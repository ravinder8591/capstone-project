from app.logger import get_logger

def test_logger_has_handlers():
    lg = get_logger("test")
    assert len(lg.handlers) >= 1