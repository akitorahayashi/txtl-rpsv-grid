from textual.widgets import Button


class CustomButton(Button):
    def __init__(self, label: str, button_id: str, info: str, **kwargs):
        super().__init__(label, variant="primary", id=button_id, **kwargs)
        self.info = info
        # フォーカスを完全に無効化
        self.can_focus = False

    def on_mount(self) -> None:
        # CSSで制御するため最小限の設定のみ
        pass
