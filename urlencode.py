import sublime
import sublime_plugin
import urllib.parse

class UrlencodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			raw = self.view.substr(sublime.Region(0, self.view.size()))
			encoded = urllib.parse.quote(raw)

			template = """--- Original ---

{}

--- URL encoded ---

{}

"""
			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(
				edit,
				0,
				template.format(raw, encoded)
			)

		except Exception as error:
			message = str(error)
			sublime.error_message(message)