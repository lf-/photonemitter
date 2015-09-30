import xdg.DesktopEntry


class DesktopEntry:
    """
    A wrapper around pyxdg's DesktopEntry to make it more pythonic
    """

    def __init__(self, filename=None, desktop_entry=None):
        """
        Create a new DesktopEntry.

        Keyword arguments:
        filename -- create a DesktopEntry from file
        desktop_entry -- create a DesktopEntry from a pyxdg DesktopEntry
        """
        self.oldde = desktop_entry or xdg.DesktopEntry.DesktopEntry(filename)

    @property
    def file(self):
        """
        The file corresponding to this DesktopEntry
        """
        return self.oldde.getFileName()

    @property
    def stripped_exec(self):
        """
        The exec key stripped of all percent variables and trailing whitespace
        """
        import re
        return ' '.join([x for x in re.split(r' +', self.exec)
                if not x.startswith('%')])

    @property
    def actions(self):
        return self.oldde.getActions()

    @property
    def categories(self):
        return self.oldde.getCategories()

    @property
    def comment(self):
        return self.oldde.getComment()

    @property
    def exec(self):
        return self.oldde.getExec()

    @property
    def generic_name(self):
        return self.oldde.getGenericName()

    @property
    def hidden(self):
        return self.oldde.getHidden()

    @property
    def icon(self):
        return self.oldde.getIcon()

    @property
    def keywords(self):
        return self.oldde.getKeywords()

    @property
    def mime_types(self):
        return self.oldde.getMimeTypes()

    @property
    def name(self):
        return self.oldde.getName()

    @property
    def not_show_in(self):
        return self.oldde.getNotShowIn()

    @property
    def only_show_in(self):
        return self.oldde.getOnlyShowIn()

    @property
    def path(self):
        return self.oldde.getPath()

    @property
    def startup_notify(self):
        return self.oldde.getStartupNotify()

    @property
    def startup_wm_class(self):
        return self.oldde.getStartupWMClass()

    @property
    def terminal(self):
        return self.oldde.getTerminal()

    @property
    def try_exec(self):
        return self.oldde.getTryExec()

    @property
    def type(self):
        return self.oldde.getType()

    @property
    def url(self):
        return self.oldde.getURL()

    @property
    def version(self):
        return self.oldde.getVersionString()
