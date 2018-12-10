# Sources
# 1. http://www.syntevo.com/doc/display/DG/Integrations
# 2. https://github.com/cbumgard/GitCommitMsg/blob/master/GitCommitMsg.py
#
# 3. https://github.com/kemayo/sublime-text-git/blob/master/git/diff.py

import sublime, sublime_plugin
import subprocess
import os

class GitLogLineCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # for region in self.view.sel():
            # row = self.view.rowcol(self.view.line(region).begin())[0] + 1
        row = self.view.rowcol(self.view.line(self.view.sel()[0]).begin())[0] + 1
        fname = self.view.file_name()
        if fname is not None:
          cmd = "git log -M35% -L " + str(row) + ",+3:" + fname
          pr = subprocess.Popen(cmd,
            cwd = os.path.dirname(self.view.file_name()),
            shell = True,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            stdin = subprocess.PIPE)
          (result, error) = pr.communicate()
          if len(result) == 0:
            result = "Ooops... Something went wrong\n\n" + str(error)
          else:
            result = result.decode("utf-8")

          new_file = self.view.window().new_file()
          new_file.insert(edit, 0, result)
          new_file.set_scratch(True)
          new_file.set_read_only(False)
          new_file.set_syntax_file("Packages/GitLogLine/logdiff.sublime-syntax")
          new_file.set_name('Line ' + str(row) + ' Log')

          sublime.status_message("")
