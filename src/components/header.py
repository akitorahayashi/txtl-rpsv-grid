from textual.widgets import Header


class AppHeader(Header):
    def __init__(self):
        super().__init__()
        self.tall = True  # ヘッダー高さ（False=1行, True=2行）
        self.icon = "✨"
        self.show_clock = True
        self.time_format = "%H:%M:%S"  # 24時間表示
        self.styles.align = ("center", "middle")
        self.styles.content_align = ("center", "middle")

    def on_mount(self) -> None:
        self.app.title = "Hello World"
        self.app.sub_title = "Textual Demo App"
