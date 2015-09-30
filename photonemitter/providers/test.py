from ..provider import Provider
from .. import output


class TestProvider(Provider):
    """
    A test provider that will always return the same thing, 3 lines from
    Still Alive

    Examples:
    >>> tp = TestProvider()
    >>> tp.query('stuff')  # doctest:+ELLIPSIS
    ['This was a triumph', ..., "It's hard to overstate my satisfaction"]
    """

    def __init__(self, **options):
        pass

    def query(self, q):
        return [output.Result(x, '') for x in ['This was a triumph',
                                               'I\'m making a note here, huge '
                                               'success', 'It\'s hard to '
                                               'overstate my satisfaction']]


class ErrorProvider(Provider):
    """
    A test provider that throws an exception.

    Examples:
    >>> ep = ErrorProvider()
    >>> ep.query('test')
    Traceback (most recent call last):
        ...
    Exception: This is a test
    """

    def __init__(self, **options):
        pass

    def query(self, q):
        raise Exception('This is a test')


if __name__ == '__main__':
    from .. import test
    test._test()
