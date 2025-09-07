from textual.binding import Binding
from textual.widgets import Footer


class AppFooter(Footer):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit", show=True),
        # 他のバインディング例:
        # Binding(key="?", action="help", description="Help", key_display="Help"),
        # Binding(key="ctrl+c", action="quit", description="Exit", show=False),
    ]

    def __init__(self):
        super().__init__()
        self.compact = False
        self.show_command_palette = True
        self.combine_groups = False
