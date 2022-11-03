import sublime
import sublime_plugin
import json

class JsonpprintCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		try:
			json_data = json.loads(self.view.substr(sublime.Region(0, self.view.size())))
			pretty = json.dumps(json_data, indent=args["indent"], sort_keys=True)
			
			self.view.erase(edit, sublime.Region(0, self.view.size()))
			self.view.insert(
				edit,
				0,
				pretty
			)

		except Exception as error:
			message = str(error)
			sublime.error_message(message)