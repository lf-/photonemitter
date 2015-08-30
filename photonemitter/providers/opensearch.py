from .. import output
from .. import provider
import requests
import urllib.parse


class OpenSearchProvider(provider.Provider):
    """
    A provider for OpenSearch compliant sites.

    This provider doesn't accept XML, so you have to translate it into JSON.
    """

    def __init__(self, search_template: str, suggestions_template: str,
                 search_cmd: str = 'xdg-open \'{url}\'', **options):
        """
        Instantiate an OpenSearchProvider.

        Templates:
        str.format() formatted strings. They accept the following format
        parameters:
            - search_term
            - url -- only for search_cmd

        Positional arguments:
        search_template -- a URL template for the search URL that is opened
                           when a result is selected. If this is falsy, disable
                           suggestions
        suggestions_template -- a URL template for the URL to query for
                                suggestions

        Keyword arguments:
        search_cmd -- a template for the command to use to open a URL
        """
        self.search_template = search_template
        self.suggestions_template = suggestions_template
        self.search_cmd = search_cmd

    def _get_search_url(self, search_term: str):
        """
        Get the search URL for the provided search term
        """
        return self.search_template.format(search_term=urllib.parse.quote(
                                             search_term))

    def _get_suggestion_url(self, search_term: str):
        """
        Get the URL for suggestions for the given search term
        """
        return self.suggestions_template.format(search_term=urllib.parse.quote(
                                                    search_term))

    def _get_search_cmd(self, search_term: str):
        """
        Get the search command for the provided search term
        """
        return self.search_cmd.format(url=self._get_search_url(search_term))

    def query(self, q: str):
        """
        Search this OpenSearchProvider

        Positional arguments:
        q -- query
        """
        if not q:
            # empty strings do not work well
            return []
        if self.suggestions_template:
            # a falsy suggestions template disables suggestions
            suggestions = requests.get(self._get_suggestion_url(q)).json()[1]
        else:
            suggestions = []
        # always insert the query as the first suggestion
        suggestions.insert(0, q)
        return (output.Result(sugg, self._get_search_cmd(sugg))
                for sugg in suggestions)
