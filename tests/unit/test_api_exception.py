"""Проверка на ожидаемые исключения из-за неправильного использования API."""

import pytest
import tasks

def test_add_raises():
    """add() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')

def test_start_tasks_db_raises():
    """Убедитесь, что не поддерживаемая БД вызывает исключение."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
