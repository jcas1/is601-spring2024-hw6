'''testing_plugin_addition'''
import pytest
from app import App

def test_app_addition_command(monkeypatch, capsys):
    '''Testing if addition correctly outputs the correct result'''
    inputs = iter(["addition 2 2", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: str(next(inputs, "exit")))

    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    assert isinstance(excinfo.value, SystemExit)

    # Check the captured output for the specific error message
    captured = capsys.readouterr()
    print("Captured Output:", captured.out)
    assert "4.0" in captured.out
