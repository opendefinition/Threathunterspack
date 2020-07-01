import sublime
import sublime_plugin
import base64

class Base64encodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			raw = self.view.substr(sublime.Region(0, self.view.size())).encode('ascii')
			encoded = base64.standard_b64encode(raw).decode('ascii')

			template = """--- Raw format ---

{}

--- Base64 encoded ---

{}

"""
			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(
				edit,
				0,
				template.format(raw.decode('utf-8'), encoded)
			)

		except Exception as error:
			message = str(error)
			sublime.error_message(message)