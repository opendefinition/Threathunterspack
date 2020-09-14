import sublime
import sublime_plugin
import re


class Ipv4extractbracketedfromtextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		document_text = self.view.substr(sublime.Region(0, self.view.size()))

		if len(document_text) > 0:
			ipv4_regex = "(\d{1,3}[\[\.\]]{3}\d{1,3}[\[\.\]]{3}\d{1,3}[\[\.\]]{3}\d{1,3})"
			ipv4_extracted = re.findall(ipv4_regex, document_text)

			if len(ipv4_extracted) > 0:
				out_text = ",\n".join(ipv4_extracted).replace("[", "").replace("]", "")

				self.view.erase(edit, sublime.Region(0, self.view.size()))
				self.view.insert(edit, 0, out_text)