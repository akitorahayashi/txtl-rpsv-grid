import os
import sys

import pytest

# srcディレクトリをパスに追加
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from components.contents import ButtonGrid, CustomButton


def test_custom_button_creation_valid():
    """CustomButtonの正常な作成をテスト"""
    button = CustomButton("テスト", "test_id", "テスト情報")
    assert button.label == "テスト"
    assert button.id == "test_id"
    assert button.info == "テスト情報"
    assert not button.can_focus
    assert button.variant == "primary"


def test_custom_button_creation_edge_cases():
    """CustomButtonのエッジケースをテスト"""
    # 長い文字列テスト
    long_text = "a" * 100
    button = CustomButton(long_text, "long_button_id", long_text)
    assert button.label == long_text
    assert button.id == "long_button_id"
    assert button.info == long_text

    # 特殊文字テスト
    special_text = "テスト!@#$%^&*()_+"
    button = CustomButton(special_text, "special_id", special_text)
    assert button.label == special_text
    assert button.info == special_text


def test_button_grid_creation_valid():
    """ButtonGridの正常な作成をテスト"""
    button_data = [
        {"label": "ボタン1", "id": "btn1", "info": "情報1"},
        {"label": "ボタン2", "id": "btn2", "info": "情報2"},
    ]
    grid = ButtonGrid(button_data)
    assert grid is not None
    assert grid.button_data == button_data
    assert hasattr(grid, "CSS_PATH")
    assert grid.CSS_PATH == "static/css/grid.css"


def test_button_grid_compose():
    """ButtonGridのcomposeメソッドをテスト"""
    button_data = [
        {"label": "ボタン1", "id": "btn1", "info": "情報1"},
        {"label": "ボタン2", "id": "btn2", "info": "情報2"},
        {"label": "ボタン3", "id": "btn3", "info": "情報3"},
    ]
    grid = ButtonGrid(button_data)
    components = list(grid.compose())

    # 正しい数のボタンが作成される
    assert len(components) == 3

    # 全てCustomButtonインスタンス
    for component in components:
        assert isinstance(component, CustomButton)

    # ボタンの内容が正しい
    for i, component in enumerate(components):
        assert component.label == button_data[i]["label"]
        assert component.id == button_data[i]["id"]
        assert component.info == button_data[i]["info"]


def test_button_grid_empty_data():
    """ButtonGridの空データテスト"""
    grid = ButtonGrid([])
    components = list(grid.compose())
    assert len(components) == 0


def test_button_grid_invalid_data():
    """ButtonGridの異常データテスト"""
    # 必要キーが欠けているデータ
    invalid_data = [{"label": "ボタン1"}]  # idとinfoが欠けている

    with pytest.raises(KeyError):
        grid = ButtonGrid(invalid_data)
        list(grid.compose())  # compose実行時にエラー


def test_button_grid_on_mount():
    """ButtonGridのon_mountメソッドをテスト"""
    grid = ButtonGrid([])

    # on_mountを直接呼び出してスタイル設定をテスト
    grid.on_mount()

    # スタイル設定が正しく適用されているか
    assert "grid" in str(grid.styles.layout)
    assert grid.styles.grid_size_columns == 3
    assert grid.styles.grid_gutter == (1, 2)
    assert grid.styles.align == ("center", "middle")
    # margin はSpacingオブジェクトなので、個別のプロパティで確認
    assert grid.styles.margin.top == 2
    assert grid.styles.margin.right == 4
    assert grid.styles.margin.bottom == 2
    assert grid.styles.margin.left == 4


if __name__ == "__main__":
    # 簡単なテスト実行
    test_custom_button_creation_valid()
    test_custom_button_creation_edge_cases()
    test_button_grid_creation_valid()
    test_button_grid_compose()
    test_button_grid_empty_data()
    test_button_grid_on_mount()
    print("All tests passed!")
