import pytest
import tasks
from tasks import Task


@pytest.mark.xfail(tasks.__version__ < '0.2.0',
                   reason='not supported until version 0.2.0')
def test_unique_id_1():
    """Вызов unique_id() дважды должен возвращать разные номера."""
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


@pytest.mark.xfail()
def test_unique_id_is_a_duck():
    """Продемонстрирация xfail."""
    uid = tasks.unique_id()
    assert uid == 'a duck'


@pytest.mark.xfail()
def test_unique_id_not_a_duck():
    """Продемонстрирация xpass."""
    uid = tasks.unique_id()
    assert uid != 'a duck'



