import pytest

from pymagecli.utils import check_extension


def test_check_extension_success():
    result = check_extension('name.jpg')
    assert result == '.jpg'
    result = check_extension('name.jpeg')
    assert result == '.jpeg'
    result = check_extension('name.png')
    assert result == '.png'


def test_check_extension_fail():
    result = check_extension('name.txt')
    assert result is None
    result = check_extension('name/')
    assert result is None


def test_check_extension_pymage_archive():
    result = check_extension('hello/pymage_archive/name.jpg')
    assert result is None
    result = check_extension('pymage_archive/name.jpg')
    assert result is None
    result = check_extension('pymage_archive/')
    assert result is None



