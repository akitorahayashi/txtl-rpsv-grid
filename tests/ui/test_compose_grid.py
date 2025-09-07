import os
import sys

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from textual.widgets import Static

from components.contents import ButtonGrid, Contents


def test_contents_compose():
    """Contentsのcomposeが正しく動作することをテスト"""
    contents = Contents()

    # composeメソッドを実行してコンポーネントを生成
    components = list(contents.compose())

    # 2つのコンポーネント（Static, ButtonGrid）があることを確認
    assert len(components) == 2
    assert isinstance(components[0], Static)
    assert isinstance(components[1], ButtonGrid)


def test_contents_button_data_structure():
    """Contentsが正しいボタンデータ構造を生成することをテスト"""
    contents = Contents()
    components = list(contents.compose())

    # ButtonGridが正しく作成されている
    button_grid = components[1]
    assert isinstance(button_grid, ButtonGrid)

    # 6つのボタンデータが設定されている
    assert len(button_grid.button_data) == 6

    # 各ボタンデータが正しい構造を持っている
    for button_data in button_grid.button_data:
        assert "label" in button_data
        assert "id" in button_data
        assert "info" in button_data


def test_contents_title_static():
    """ContentsのStaticタイトルが正しく設定されることをテスト"""
    contents = Contents()
    components = list(contents.compose())

    # 最初のコンポーネントがStaticタイトル
    title_static = components[0]
    assert isinstance(title_static, Static)
    # classesはfrozensetなので、containsで確認
    assert "title" in title_static.classes


if __name__ == "__main__":
    # 簡単なテスト実行
    test_contents_compose()
    test_contents_button_data_structure()
    test_contents_title_static()
    print("All Contents tests passed!")
