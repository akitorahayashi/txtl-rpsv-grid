from textual.containers import Vertical
from textual.widgets import Button, Static

from .button import CustomButton
from .grid import ButtonGrid


class Contents(Vertical):
    def compose(self):
        # タイトル - 直接スタイルを設定
        title = Static("ボタンをクリックしてください。", classes="title")
        title.styles.text_align = "center"
        title.styles.margin = (2, 4, 0, 4)
        title.styles.padding = (1, 4)
        title.styles.width = "100%"
        yield title

        # ボタンデータ定義
        button_data = [
            {
                "label": "ボタン1",
                "id": "btn1",
                "info": "これは1番目のボタンです。左上に配置されています。",
            },
            {
                "label": "ボタン2",
                "id": "btn2",
                "info": "これは2番目のボタンです。上段中央に配置されています。",
            },
            {
                "label": "ボタン3",
                "id": "btn3",
                "info": "これは3番目のボタンです。右上に配置されています。",
            },
            {
                "label": "ボタン4",
                "id": "btn4",
                "info": "これは4番目のボタンです。左下に配置されています。",
            },
            {
                "label": "ボタン5",
                "id": "btn5",
                "info": "これは5番目のボタンです。下段中央に配置されています。",
            },
            {
                "label": "ボタン6",
                "id": "btn6",
                "info": "これは6番目のボタンです。右下に配置されています。",
            },
        ]

        # ButtonGridコンポーネントで責務分離
        yield ButtonGrid(button_data)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # CustomButtonのinfoプロパティとIDを使用して適切に処理
        button = event.button
        if isinstance(button, CustomButton) and hasattr(button, "info"):
            self.app.notify(
                title=f"{button.label} (ID: {button.id}) がクリックされました！",
                message=button.info,
                timeout=3.0,
            )
        else:
            # フォールバック処理
            self.app.notify(
                title=f"ボタン {button.id} がクリックされました！",
                message=f"ラベル: {button.label}",
                timeout=3.0,
            )
