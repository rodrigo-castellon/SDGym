import sys

from sdgym.utils import get_size


def test_get_size():
    """Test that the correct size is returned."""
    # Setup
    test_obj = {'key': 'value'}

    # Run
    size = get_size(test_obj)

    # Assert
    size == sys.getsizeof(test_obj)


def test_get_size_nested_obj():
    """Test that the correct size is returned when given a nested object."""
    # Setup
    test_inner_obj = {'inner_key': 'inner_value'}
    test_obj = {'key1': 'value', 'key2': test_inner_obj}

    # Run
    size = get_size(test_obj)

    # Assert
    size == sys.getsizeof(test_obj) + sys.getsizeof(test_inner_obj)
