import sublime
import sublime_plugin
import os

from os import path

class LoadtemplateCommand(sublime_plugin.TextCommand):
	def run(self, edit, **args):
		template_path = os.path.join(
			os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
			args['module'],
			'{}.tpl'.format(args['template'])
		)

		if path.exists(template_path):
			with open(template_path, 'r') as template_file:
				content = template_file.read()
				template_file.close()

				self.view.insert(
					edit,
					self.view.sel()[0].begin(),
					content
				)
		else:
			message = "Unable to find template:\n\n{}\n\nPlease check if template exists!".format(template_path)
			sublime.error_message(message)