"""Test tasks.unique_id()."""

import pytest
import tasks

from tasks import Task


@pytest.mark.skip(reason='misunderstood the API')
def test_unique_id_1():
    """Вызов unique_id () дважды должен возвращать разные числа."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    """unique_id() должен вернуть неиспользуемый id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))
    # захват уникального id
    uid = tasks.unique_id()
    # убеждаемся, что его нет в списке существующих идентификаторов
    assert uid not in ids



