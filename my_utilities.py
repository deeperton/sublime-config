import sublime, sublime_plugin

class MyExpandSelectionWithSameCase(sublime_plugin.TextCommand):
    def run(self, edit):
        regions = []
        for s in self.view.sel():
            line = self.view.line(sublime.Region(s.begin(), s.end()))
            if line.end() == s.end():
                # we're at the end of a line, so select the next line
                line = self.view.line(sublime.Region(s.end(), s.end() + 1))
            regions.append(line)
        for r in regions:
            self.view.sel().add(r)
