"""End-to-end tests for launching the Textual application."""

import subprocess
import sys
from pathlib import Path

import pytest


def test_app_launches_successfully():
    """Test that the main application launches without errors."""
    # Get the path to the main application file
    project_root = Path(__file__).parent.parent.parent
    main_py_path = project_root / "src" / "main.py"

    # Run the application with a timeout to prevent hanging
    try:
        result = subprocess.run(
            [sys.executable, str(main_py_path)],
            timeout=3,
            capture_output=True,
            text=True,
            cwd=project_root,
        )
    except subprocess.TimeoutExpired:
        pass
    else:
        if result.returncode != 0:
            pytest.fail(f"Application failed to start: {result.stderr}")


def test_app_imports_correctly():
    """Test that the main application can be imported without errors."""
    project_root = Path(__file__).parent.parent.parent

    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys; sys.path.insert(0, 'src'); import main; print('Import successful')",
        ],
        capture_output=True,
        text=True,
        cwd=project_root,
    )

    assert result.returncode == 0, f"Import failed: {result.stderr}"
    assert "Import successful" in result.stdout


def test_textual_dependency_available():
    """Test that the Textual dependency is properly installed."""
    result = subprocess.run(
        [sys.executable, "-c", "import textual; print(textual.__version__)"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, f"Textual import failed: {result.stderr}"
    assert result.stdout.strip(), "Textual version should be displayed"
