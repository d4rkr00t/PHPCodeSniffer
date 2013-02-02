import sublime, sublime_plugin
import subprocess

class PhpCodeSniffer(sublime_plugin.WindowCommand):
	def run(self):



		cur_view = self.window.active_view()

		if "php" in cur_view.syntax_name(cur_view.sel()[0].b):

			settings = sublime.load_settings('PHPCodeSniffer.sublime-settings')

			try:
				p = subprocess.Popen(settings.get('phpcs')[sublime.platform()]+" \""+str(cur_view.file_name())+"\"", shell=True, stdout=subprocess.PIPE)
				out, err = p.communicate()
				view = self.window.new_file()
				edit = view.begin_edit()
				view.insert(edit, 0, out)
			except Exception, e:
				print e

		else:
			sublime.error_message("File must be .php")
			raise Exception("File must be .php")
		
		return True