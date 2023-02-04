"""Проверка на ожидаемые исключения из-за неправильного использования API."""

import pytest
import tasks


def test_add_raises():
    """add() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


def test_start_tasks_db_raises():
    """Не поддерживаемая БД должна вызывать исключение."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_raises():
    """list() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate:
    """Тест ожидаемых исключений с tasks.update()."""

    def test_bad_id(self):
        """non-int id должен поднять exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task должен поднять exception."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')
