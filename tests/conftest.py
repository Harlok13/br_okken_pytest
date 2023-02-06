"""Placeholder."""
import pytest
import tasks
from tasks import Task


# nothing here yet

# Памятка об интерфейсе Task constructor
# Task(summary=None, owner=None, done=False, id=None)
# summary то что требуется
# owner и done являются необязательными
# id задается базой данных

@pytest.fixture()
def tasks_just_a_few():
    """Все резюме и владельцы уникальны."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def tasks_mult_per_owner():
    """Несколько владельцев с несколькими задачами каждый."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # здесь происходит тестирование

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def db_with_3_tasks(initialized_tasks_db, tasks_just_a_few):
    """Подключение БД с 3 задачами, все уникальны."""
    for t in tasks_just_a_few:
        tasks.add(t)

@pytest.fixture()
def db_with_multi_per_owner(initialized_tasks_db, tasks_mult_per_owner):
    """Подключение БД с 9 задачами, 3 owners, с 3 задачами у каждого."""
    for t in tasks_mult_per_owner:
        tasks.add(t)
