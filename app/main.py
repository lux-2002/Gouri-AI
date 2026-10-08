from app.config.settings import Settings
from app.core.assistant import VoiceAssistant
from app.tools.browser import BrowserTool
from app.tools.jokes import JokeTool
from app.tools.music import MusicTool
from app.tools.system import ExitTool, TimeTool


def build_assistant() -> VoiceAssistant:
    settings = Settings()

    tools = [
        TimeTool(),
        BrowserTool(),
        JokeTool(),
        MusicTool(settings.music_directory),
        ExitTool(),
    ]

    return VoiceAssistant(settings=settings, tools=tools)


def main() -> None:
    assistant = build_assistant()
    assistant.run()


if __name__ == "__main__":
    main()
