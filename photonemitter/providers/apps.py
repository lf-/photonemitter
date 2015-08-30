from .. import util
from .. import provider
from .. import output
import fuzzywuzzy.process
import fuzzywuzzy.fuzz


class AppsProvider(provider.Provider):
    """
    A provider for XDG applications.
    """

    def __init__(self, icon_theme: str = None,
                 score_threshold: int = 15, **options):
        """
        Instantiate an AppsProvider

        Keyword arguments:
        icon_theme -- icon theme on which to perform icon lookups
        score_threshold -- ignore results below this score threshold.
                           Range: 0-100 (see score cutoffs for fuzzywuzzy)
        """
        self.icon_theme = icon_theme
        self.score_threshold = score_threshold

    def query(self, q: str) -> list:
        """
        Search for an application, return Results

        Examples:
        >>> ap = AppsProvider()
        >>> ap.query('firefox') #doctest:+SKIP
        [Result('Firefox', '/usr/bin/firefox',
                img='/usr/share/icons/.../firefox.png')]
        """
        results = []
        for res in self._search(q):
            results.append(output.Result(res.getName(), res.getExec(),
                                         util.get_icon_file(res.getIcon(),
                                         icon_theme=self.icon_theme)))
        return results

    def _search(self, q: str,
                desktop_entries=util.desktop_entries) -> list:
        denames = {e.getName(): e for e in desktop_entries}
        results = fuzzywuzzy.process.extractBests(
                q,
                list(denames),
                score_cutoff=self.score_threshold,
                scorer=fuzzywuzzy.fuzz.QRatio
        )
        results = [denames[res[0]] for res in results]
        return results
