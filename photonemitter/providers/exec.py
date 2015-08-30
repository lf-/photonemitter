from .. import output
from .. import provider


class ExecProvider(provider.Provider):
    """
    A provider for executing commands.
    """

    def __init__(self, terminal_cmd=None, **options):
        """
        Instantiate an ExecProvider.

        Keyword arguments:
        terminal_cmd -- command to run to open a terminal running the command.
                        {cmd} is used to insert the command. For example,
                        "urxvt -e '{cmd}'"
        """
        self.terminal_cmd = terminal_cmd

    def query(self, q):
        """
        Generate standard "results" for commands.

        Positional arguments:
        query -- command to execute

        Examples:
        >>> ep = ExecProvider()
        >>> ep.query('echo y')
        [Result("Execute 'echo y'", 'echo y', img=None)]

        >>> ep = ExecProvider(terminal_cmd="urxvt -e '{cmd}'")
        >>> ep.query('echo y')
        [Result("Execute 'echo y'", 'echo y', img=None), Result("Run 'echo y' \
in a terminal", "urxvt -e 'echo y'", img=None)]
        """
        results = [output.Result('Execute \'{cmd}\''.format(cmd=q), q)]
        if self.terminal_cmd:
            results.append(output.Result('Run \'{cmd}\' in a terminal'.format(
                                             cmd=q
                                         ),
                                         self.terminal_cmd.format(cmd=q)))
        return results


if __name__ == '__main__':
    from .. import test
    test._test()
