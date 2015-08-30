from .. import output
from .. import provider
import subprocess


class CalcProvider(provider.Provider):
    """
    A Provider for a calculator.
    """

    def __init__(self, **kwargs):
        """
        Instantiate a CalcProvider
        """

    def _evaluate(self, expr: str):
        """Evaluate the provided bc expression"""
        return subprocess.check_output(
            ['bc'],
            input='{}\n'.format(expr).encode(),
            stderr=subprocess.STDOUT
        )[:-1].decode('utf-8')

    def query(self, q: str) -> list:
        """
        Do the math operation provided.

        Positional arguments:
        q -- query
        """
        return [output.Result(self._evaluate(q), '')]
