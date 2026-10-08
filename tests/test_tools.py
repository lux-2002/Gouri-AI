from app.tools.browser import BrowserTool
from app.tools.jokes import JokeTool
from app.tools.system import ExitTool, TimeTool


def test_time_tool():
    result = TimeTool().execute("what time is it")
    assert "current time is" in result.lower()


def test_exit_tool():
    result = ExitTool().execute("exit")
    assert "goodbye" in result.lower()


def test_joke_tool():
    result = JokeTool().execute("tell me a joke")
    assert isinstance(result, str)
    assert result


def test_browser_tool_recognizes_youtube():
    assert BrowserTool().can_handle("open youtube")
