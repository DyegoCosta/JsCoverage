import sublime
import sublime_plugins

def highlight_lines(view):
	lines = view.lines(sublime.Region(0, view.size()))

class JsCoverageCommand(sublime_plugin.WindowCommand):
	def run(self):
		highlight_lines(self.window.active_view())

class JsCoverageListener(sublime_plugin.EventListener):
	def on_modified(self, view):
        if plugin_enabled:
            highlight_duplicates(view)

    def on_activated(self, view):
        if plugin_enabled:
            highlight_duplicates(view)

    def on_load(self, view):
        if plugin_enabled:
            highlight_duplicates(view)