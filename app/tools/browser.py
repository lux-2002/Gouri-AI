import webbrowser

from app.tools.base import AssistantTool


class BrowserTool(AssistantTool):
    def __init__(self, college_url: str = "https://www.cmrit.ac.in/"):
        self.college_url = college_url

    @property
    def name(self) -> str:
        return "browser"

    def can_handle(self, text: str) -> bool:
        normalized = text.lower()
        return (
            "youtube" in normalized
            or normalized in {"open web", "open browser", "open college website"}
        )

    def execute(self, text: str) -> str:
        normalized = text.lower()

        if "youtube" in normalized:
            webbrowser.open("https://www.youtube.com/")
            return "Opening YouTube."

        webbrowser.open(self.college_url)
        return "Opening the configured website."
