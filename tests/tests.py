#TODO
# All we need to do is to implement the fixture into the functions instead
# of doing the creation and deletion each time. We could also add more
# edge cases / exceptions stuff if you find it but I don't think
# it is necessary

from pmgr.project import Project, TaskException
import pytest
import os

"""
@pytest.fixture(scope="function")
def create_class():
    c = Project("trial")
    yield c
    os.remove(c.filepath)
    del c
"""

def test_class_init():
    c = Project("trial")
    assert c.name == "trial"
    os.remove(c.filepath)
    del c
    

def test_add_task():
    c = Project("trial")
    c.add_task("first")
    assert c.get_tasks() == ["first"]
    os.remove(c.filepath)
    del c

def test_fail_add_task():
    c = Project("trial")
    c.add_task("first")
    with pytest.raises(TaskException):
        c.add_task("first")
    os.remove(c.filepath)

def test_remove_task():
    c = Project("trial")
    c.add_task("first")
    c.add_task("second")
    c.remove_task("first")
    assert c.get_tasks() == ["second"]
    os.remove(c.filepath)

def test_fail_remove_task():
    c = Project("trial")
    c.add_task("first")
    c.add_task("second")
    with pytest.raises(TaskException):
        c.remove_task("third")
    os.remove(c.filepath)

def test_get_tasks():
    c = Project("trial")
    c.add_task("first")
    c.add_task("second")
    assert c.get_tasks() == ["first", "second"]
    os.remove(c.filepath)
