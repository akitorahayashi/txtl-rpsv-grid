from textual.containers import Grid

from .button import CustomButton


class ButtonGrid(Grid):
    CSS_PATH = "static/css/grid.css"

    def __init__(self, button_data: list, **kwargs):
        super().__init__(**kwargs)
        self.button_data = button_data

    def compose(self):
        # 公式Grid構成：ボタンを順番にyield、Gridが自動配置
        for data in self.button_data:
            yield CustomButton(data["label"], data["id"], data["info"])

    def on_mount(self) -> None:
        # PythonでもGrid設定を明示的に追加
        self.styles.layout = "grid"
        self.styles.grid_size_columns = 3
        self.styles.grid_gutter = (1, 2)
        self.styles.align = ("center", "middle")
        self.styles.margin = (2, 4)
