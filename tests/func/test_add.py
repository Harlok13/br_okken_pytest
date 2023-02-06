"""Проверьте функцию API tasks.add ()."""

import pytest
import tasks
from tasks import Task


def test_add_returns_valid_id(initialized_tasks_db):
    """tasks.add(<valid task>) должен возвращать целое число."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN returned task_id is of type int
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    """Убедимся, что поле task_id установлено tasks.add()."""
    # GIVEN an initialized tasks db
    # AND a new task is added
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    # WHEN task is retrieved
    task_from_db = tasks.get(task_id)

    # THEN task_id matches id field
    assert task_from_db.id == task_id


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() должен повлиять на task.count()."""
    # GIVEN db с 3 задачами
    # WHEN добавляется еще одна задача
    tasks.add(Task('throw a party'))

    # THEN счетчик увеличивается на 1
    assert tasks.count() == 4
