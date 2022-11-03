import sublime
import sublime_plugin

class SplittextCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		delimiter = args['delimiter']
		replacer = args['replacer']

		document_text = self.view.substr(sublime.Region(0, self.view.size())).replace(delimiter, replacer)

		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(
			edit,
			0,
			document_text
		)