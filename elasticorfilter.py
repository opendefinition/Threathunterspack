import sublime
import sublime_plugin

class ElasticorfilterCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		full_select = sublime.Region(0, self.view.size())
		splitted = self.view.split_by_newlines(full_select)

		text_archive = []

		for text_line in splitted:
			text = self.view.substr(text_line)

			if text not in text_archive and len(text) > 0:
				text_archive.append("\"{}\"".format(text))

		text_archive.sort()

		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(
			edit,
			0,
			" OR ".join(text_archive)
		)