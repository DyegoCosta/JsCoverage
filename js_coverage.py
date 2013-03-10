import sublime
import sublime_plugin
from collections import defaultdict

DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = False

settings = sublime.load_settings('js_coverage.sublime-settings')
plugin_enabled = bool(settings.get('js_coverage_enabled', DEFAULT_IS_ENABLED))

def cover(view):
    ## run_all_tests()

    ## log = read_coverage_log()

    ## highlight_uncovered_lines(log)

    ## highlight_covered_lines(log)


    regions = view.lines(sublime.Region(0, view.size()))
    
    color_scope_name = settings.get('highlight_color',
                                        DEFAULT_COLOR_SCOPE_NAME)

    view.add_regions('JsCoverageListener',
                        regions, color_scope_name,
                        sublime.PERSISTENT)

def uncover(window):
    for view in window.views():
        view.erase_regions('JsCoverageListener')

class JsCoverageCommand(sublime_plugin.WindowCommand):
    def run(self):
        cover(self.window.active_view()) if plugin_enabled else uncover(self.window)

class JsCoverageListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        if plugin_enabled: cover(view)

    def on_activated(self, view):
        if plugin_enabled: cover(view)

    def on_load(self, view):
        if plugin_enabled: cover(view)

class ToggleJsCoverageCommand(sublime_plugin.WindowCommand):
    def run(self):
        global plugin_enabled
        plugin_enabled = False if plugin_enabled else True

        if plugin_enabled:
            cover(self.window.active_view())
        else:
            uncover(self.window)