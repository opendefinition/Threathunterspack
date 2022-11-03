import sublime
import sublime_plugin
import urllib.parse

class UrldecodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			encoded = self.view.substr(sublime.Region(0, self.view.size()))
			decoded = urllib.parse.unquote(encoded)

			template = """--- Encoded ---

{}

--- URL decoded ---

{}

"""
			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(
				edit,
				0,
				template.format(encoded, decoded)
			)

		except Exception as error:
			message = str(error)
			sublime.error_message(message)