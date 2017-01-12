import sublime
import sublime_plugin

# view.run_command('DarkLightModeSwitch')
# view.run_command('darklightmodeswitch')

class DarklightmodeswitchCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        settings = sublime.load_settings("Preferences.sublime-settings")
        current_color_scheme = settings.get("color_scheme")

        if current_color_scheme == "Packages/User/SublimeLinter/Solarized (Dark) (SL).tmTheme":
            color_scheme = "Packages/User/SublimeLinter/Solarized (Light) (SL).tmTheme"
        else:
            color_scheme = "Packages/User/SublimeLinter/Solarized (Dark) (SL).tmTheme"

        settings.set("color_scheme", color_scheme)
        
        sublime.save_settings("Preferences.sublime-settings")

        self.log_to_console("current colour scheme: ´" + current_color_scheme)

    def log_to_console(self, arg):
        arg = str(arg)
        print(arg)
