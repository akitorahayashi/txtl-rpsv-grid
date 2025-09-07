from textual.app import App, ComposeResult
from textual.binding import Binding

from components.contents import Contents
from components.footer import AppFooter
from components.header import AppHeader


class HelloWorldApp(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit", show=True),
    ]

    def compose(self) -> ComposeResult:
        yield AppHeader()
        yield Contents()
        yield AppFooter()
