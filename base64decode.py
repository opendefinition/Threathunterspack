import sublime
import sublime_plugin
import base64

class Base64decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			encoded = self.view.substr(sublime.Region(0, self.view.size()))
			decoded = base64.standard_b64decode(encoded).decode('utf-8')

			template = """--- Encoded ---

{}

--- Decoded ---

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