import sublime, sublime_plugin, subprocess, json, os
from glob import glob

COVERAGE_LOG_PATH = os.path.abspath("coverage") + "\coverage-PhantomJS*.json"
DEFAULT_COLOR_SCOPE_NAME = "invalid"
DEFAULT_IS_ENABLED = False

settings = sublime.load_settings('js_coverage.sublime-settings')
plugin_enabled = bool(settings.get('js_coverage_enabled', DEFAULT_IS_ENABLED))

def cover(view):
    run_tests()

    sublime.set_timeout(lambda: highlight(view), 6000)

def uncover(window):
    for view in window.views():
        view.erase_regions('JsCoverageListener')

def run_tests():
    sublime.status_message("Running tests and generating coverage")
    subprocess.Popen("testacular start \"config/testacular.conf.js\"", stdout=subprocess.PIPE, shell=True)

def highlight(view):
    log = get_coverage_log()

    delete_log()

    highlight_uncovered_lines(log)

    highlight_covered_lines(log)

    regions = view.lines(sublime.Region(0, view.size()))
    
    color_scope_name = settings.get('highlight_color', DEFAULT_COLOR_SCOPE_NAME)

    view.add_regions('JsCoverageListener',
                        regions, color_scope_name,
                        sublime.PERSISTENT)

def get_coverage_log():
    print get_log_path()
    log = open(get_log_path()).read()

    return json.loads(log)

def delete_log():
    os.remove(get_log_path())    

def get_log_path():
    return glob(COVERAGE_LOG_PATH)[0]

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
