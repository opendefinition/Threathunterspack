import sublime
import sublime_plugin
import base64

class Base64decodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			encoded = self.view.substr(sublime.Region(0, self.view.size()))
			b64_decoded = base64.standard_b64decode(encoded)

			encodings = {
				"latin1": None,
				"utf-8": None,
				"utf-16": None
			}


			template = []
			template.append("## Base64 Encoded\n\n{}\n".format(encoded))

			for encoding in encodings.keys():
				decoded = b64_decoded.decode(encoding)
				template.append("\n### Decoded as {}\n\n{}\n".format(encoding,decoded))

			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(
				edit,
				0,
				"".join(template)
			)

		except Exception as error:
			message = str(error)
			sublime.error_message(message)