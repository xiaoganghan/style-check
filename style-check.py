# Check English writing style

import os
import sublime, sublime_plugin, urllib.request, urllib.parse, re
from .checker import get_rules, match

class StyleCheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if len(self.view.sel()) == 1 and self.view.sel()[0].a == self.view.sel()[0].b:
            self.view.run_command("expand_selection", {"to": "word"})

        for sel in self.view.sel():
            if sel.empty():
                continue

            fix = self.correct(self.view.substr(sel))
            # self.view.replace(edit, sel, fix)
            self.view.end_edit(edit)

    def correct(self, text):
        rules = get_rules()
        problems = match(get_rules(), text)
        for problem in problems:
            print(problem)

        return ''

