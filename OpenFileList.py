import sublime, sublime_plugin
import os.path

class OpenFileListCommand(sublime_plugin.WindowCommand):
    def run(self):
        views = self.window.views()
        names = []
        for view in views:
            name = view.file_name()
            if not name:
                name = view.name()
            names.append([os.path.basename(name)])
        self.window.show_quick_panel(names, self.on_done)

    def on_done(self, index):
        if index >= 0:
            num_groups = self.window.num_groups()
            for group_id in range(num_groups):
                views = self.window.views_in_group(group_id)
                views_count = len(views)
                if index < views_count:
                    self.window.focus_group(group_id)
                    self.window.focus_view(views[index])
                    break
                else:
                    index = index - views_count

    def is_enabled(self):
        return self.window.active_view() != None
