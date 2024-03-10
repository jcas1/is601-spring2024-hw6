'''testing_plugin_subtraction'''
import pytest
from app import App

def test_app_subtraction_command(monkeypatch, capsys):
    '''Testing if subtraction correctly outputs the correct result'''
    inputs = iter(["subtraction 2 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: str(next(inputs, "exit")))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    assert isinstance(excinfo.value, SystemExit)

    # Check the captured output for the specific error message
    captured = capsys.readouterr()
    print("Captured Output:", captured.out)
    assert "0.0" in captured.out
