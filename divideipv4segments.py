import sublime
import sublime_plugin
import re

class Divideipv4segmentsCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		full_select = sublime.Region(0, self.view.size())
		splitted = self.view.split_by_newlines(full_select)

		text_archive = []

		for text_line in splitted:
			text = self.view.substr(text_line)

			if text not in text_archive:
				text_archive.append(text)

		text_archive.sort()

		prev_segment = ""
		for index, ip in enumerate(text_archive):
			segment_search = re.search(r"(^\d{1,3}\.\d{1,3}\.\d{1,3})", ip)

			if segment_search:
				segment = segment_search.group()
	
				if segment != prev_segment and index > 0:
					text_archive[index] = "\n{}".format(ip)

				prev_segment = segment

				self.view.erase(edit, sublime.Region(0, self.view.size()))
				self.view.insert(
					edit,
					0,
					"\n".join(text_archive)
				)