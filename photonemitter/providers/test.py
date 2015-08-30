from .. import provider
from .. import output


class TestProvider(provider.Provider):
    """
    A test provider that will always return the same thing, 3 lines from
    Still Alive

    Examples:
    >>> tp = TestProvider('.*')
    >>> tp.query('stuff')  # doctest:+ELLIPSIS
    ['This was a triumph', ..., "It's hard to overstate my satisfaction"]
    """

    def __init__(self, match, **options):
        self.match = match

    def query(self, q):
        return [output.Result(x, '') for x in ['This was a triumph',
                                               'I\'m making a note here, huge '
                                               'success', 'It\'s hard to '
                                               'overstate my satisfaction']]


if __name__ == '__main__':
    from .. import test
    test._test()
