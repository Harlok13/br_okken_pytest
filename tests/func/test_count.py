import pytest
import tasks
from tasks import Task


def test_count_returns_valid_value():
    """tasks.count(valid task) должен возвращать целое число."""
    count_tasks_db = tasks.count()
    assert isinstance(count_tasks_db, int)


def test_count_of_empty_db():
    """tasks.count(valid task) пустая бд должна возвращать 0."""
    count_tasks_db = tasks.count()
    assert count_tasks_db == 0


tasks_to_try = [(Task('wake up', 'Harlok', False),
                 Task('sleep', None, False)),

                (Task('walk', 'HarloK', True),),

                (Task('dream', None, False),
                 Task('eat', 'HARLOK', True),
                 Task('drink', 'Harlok', False))
                ]


def task_ids(tasks_to_try):
    """Создает список для ids test_count_of_not_empty_db."""
    list_of_task_ids = []
    for element in tasks_to_try:
        current_list = []
        for t in element:
            message = f'Task({t.summary}, {t.owner}, {t.done})'
            current_list.append(message)
        list_of_task_ids.append(', '.join(current_list))
    return list_of_task_ids


@pytest.mark.parametrize('task', tasks_to_try, ids=task_ids(tasks_to_try))
def test_count_of_not_empty_db(task):
    """tasks.count(valid task) не пустая бд должна возвращать правильное число записей."""
    [tasks.add(tsk) for tsk in task]
    tasks_db = tasks.count()
    expected_count = len(task)
    assert tasks_db == expected_count


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # здесь происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()
