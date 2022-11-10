import sublime
import sublime_plugin

class ElasticregexifytextCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sel = self.view.sel()[0]
		selected = self.view.substr(sel).strip()

		replacements = [
			".",
			"^",
			"$",
			"*",
			"+",
			"-",
			"?",
			"(",
			")",
			"[",
			"]",
			"{",
			"}",
			"\""
		]

		legal = [
			"_",
			":",
			"&",
			"%",
			"|",
		]
		
		char_regx = ""
		for char in selected:
			if char.isdigit() or char in legal:
				char_regx += char
			elif char is " ":
				char_regx += ".{1}"
			elif char is "\\":
				char_regx += "\\\\"
			elif char in replacements:
				char_regx += "\\{character}".format(character=char)
			else:
				char_regx += "[{up}{lo}]".format(lo=char.lower(), up=char.upper())

		self.view.replace(edit, sel, "/.*{chars}.*/".format(chars=char_regx))