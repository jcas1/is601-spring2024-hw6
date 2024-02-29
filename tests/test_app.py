'''App Testing'''
#pylint: disable=unused-variable
import pytest
from app import App

def test_app_start_exit_input(monkeypatch, capsys):
    '''Testing that program exits correctly'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_invalid_input(monkeypatch, capsys):
    '''Testing For invalid input'''
    invalid_inputs = iter(["not_valid", "2", "2"])
    monkeypatch.setattr('builtins.input', lambda _: str(next(invalid_inputs, "exit")))
    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    captured = capsys.readouterr()
    assert "Invalid input format. Please enter [operation x y]" in captured.out

def test_app_divide_by_zero(monkeypatch, capsys):
    '''Testing For division by zero'''
    inputs = iter(["division 2 0", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: str(next(inputs, "exit")))
    app = App()

    with pytest.raises(SystemExit) as excinfo:
        app.start()

    assert isinstance(excinfo.value, SystemExit)

    # Check the captured output for the specific error message
    captured = capsys.readouterr()
    print("Captured Output:", captured.out)
    assert "Cannot divide by zero!!!" in captured.out
