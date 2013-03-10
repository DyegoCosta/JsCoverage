import sublime
import sublime_plugin
from collections import defaultdict

DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = True

settings = sublime.load_settings('js_coverage.sublime-settings')
plugin_enabled = bool(settings.get('js_coverage_enabled', DEFAULT_IS_ENABLED))

def highlight_lines(view):
    lines = view.lines(sublime.Region(0, view.size()))    
    
    counts = defaultdict(list)
    for line in lines:
        string = view.substr(line).strip()
        counts[string].append(line)

    show_lines(counts.values(), view)

def show_lines(regions, view):
    all_regions = []

    for r in regions:
        all_regions.extend(r)

    color_scope_name = settings.get('highlight_color',
                                        DEFAULT_COLOR_SCOPE_NAME)

    view.add_regions('JsCoverageListener',
                        all_regions, color_scope_name,
                        sublime.DRAW_OUTLINED)

def downlight_lines(window):
    for view in window.views():
        view.erase_regions('JsCoverageListener')

class JsCoverageCommand(sublime_plugin.WindowCommand):
    def run(self):
        if plugin_enabled:
            highlight_lines(self.window.active_view())
        else:
            downlight_lines(self.window)

class JsCoverageListener(sublime_plugin.EventListener):
    def on_modified(self, view):
        if plugin_enabled:
            highlight_lines(view)

    def on_activated(self, view):
        if plugin_enabled:
            highlight_lines(view)

    def on_load(self, view):
        if plugin_enabled:
            highlight_lines(view)

class ToggleJsCoverageCommand(sublime_plugin.WindowCommand):
    def run(self):
        global plugin_enabled
        plugin_enabled = False if plugin_enabled else True

        if plugin_enabled:
            highlight_lines(self.window.active_view())
        else:
            downlight_lines(self.window)