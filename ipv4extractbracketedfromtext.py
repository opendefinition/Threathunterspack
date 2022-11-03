import sublime
import sublime_plugin
import re


class Ipv4extractbracketedfromtextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		document_text = re.sub(
				r"[\[\]\<\>a-zA-Z]",
				"",
				self.view.substr(sublime.Region(0, self.view.size()))
			)

		if len(document_text) > 0:
			splitted = document_text.split("\n")
			findings = []

			for line in splitted:
				item = line.replace(" ", "")

				ipv4_regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
				ipv4_extracted = re.findall(ipv4_regex, item)

				if len(ipv4_extracted) > 0:
					if ipv4_extracted[0] not in findings:
						findings.append(ipv4_extracted[0])

			out_text = "\n".join(findings)
			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(edit, 0, out_text)