# Gouri AI — Hybrid Voice Intelligence Assistant

> **Evolution of a 3rd-year engineering project into a modular Python + AI engineering system.**

Gouri AI is a voice-driven personal assistant rebuilt from an early college project into a modular, extensible application combining:

- Speech-to-text
- Text-to-speech
- Intent routing
- Deterministic tool execution
- Optional LLM fallback
- Conversation context
- Structured logging
- Command latency tracking
- Testable Python components
- Environment-based configuration
- Docker-ready packaging

The design intentionally uses a **hybrid architecture**: deterministic commands are handled locally and predictably, while ambiguous natural-language requests can be delegated to an LLM.

---

## Why this project was rebuilt

The original 3rd-year implementation was a simple rule-based voice assistant using `speech_recognition`, `pyttsx3`, browser automation and hard-coded `if/elif` commands.

This version treats that project as an engineering evolution:

**College prototype → modular Python system → AI-assisted intent handling → observable, testable application**

This makes the project useful as evidence of Python, AI integration, software design and production-oriented engineering fundamentals.

---

## Architecture

```text
                         ┌──────────────────────┐
                         │      Microphone      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   SpeechRecognizer   │
                         │  speech → text       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │     IntentRouter     │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┴────────────────┐
                    │                                │
             Known command                    Unknown request
                    │                                │
                    ▼                                ▼
             ┌─────────────┐                 ┌─────────────┐
             │ Local Tools │                 │ LLM Fallback│
             └──────┬──────┘                 └──────┬──────┘
                    │                               │
                    └──────────────┬────────────────┘
                                   ▼
                         ┌──────────────────────┐
                         │ ConversationContext │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │  SpeechSynthesizer   │
                         │  text → speech       │
                         └──────────────────────┘
```

---

## Project structure

```text
gouri-ai/
├── app/
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── intent_classifier.py
│   │   ├── llm_client.py
│   │   └── response_generator.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── assistant.py
│   │   ├── context.py
│   │   ├── exceptions.py
│   │   └── router.py
│   ├── speech/
│   │   ├── __init__.py
│   │   ├── recognizer.py
│   │   └── synthesizer.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── browser.py
│   │   ├── jokes.py
│   │   ├── music.py
│   │   └── system.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   └── main.py
├── tests/
│   ├── test_context.py
│   ├── test_intent_classifier.py
│   ├── test_router.py
│   └── test_tools.py
├── docs/
│   └── architecture.md
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## Core design decisions

### 1. Hybrid routing

Not every request needs an LLM.

Examples:

```text
"What time is it?"
        ↓
Local system tool

"Open YouTube"
        ↓
Browser tool

"Tell me something interesting about AI agents."
        ↓
Optional LLM fallback
```

This reduces unnecessary API calls and keeps deterministic actions predictable.

### 2. Tool-based architecture

Capabilities are isolated into tools rather than embedded inside the assistant loop.

Adding a new capability therefore becomes a localized change instead of expanding a large `if/elif` block.

### 3. Conversation context

Recent user/assistant messages are stored in a bounded context window so an LLM can receive relevant conversation history without allowing memory to grow indefinitely.

### 4. Observability

Every routed command records:

- input
- intent
- selected tool
- execution status
- latency
- timestamp

This creates a foundation for later analytics and performance benchmarking.

---

## Supported commands

The current local tool set includes:

| Command family | Examples |
|---|---|
| Time | "What time is it?" |
| YouTube | "Open YouTube" |
| Browser | "Open web" / "Open college website" |
| Jokes | "Tell me a joke" |
| Music | "Play a song" |
| Exit | "Exit", "quit", "goodbye" |

Unknown requests can use the optional LLM fallback.

---

## Installation

### Requirements

- Python 3.10+
- Working microphone
- Speakers/headphones
- Internet connection for Google Speech Recognition
- Windows is recommended for the local music launcher because the project supports `os.startfile`

### Install

```bash
git clone <your-repository-url>
cd gouri-ai

python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Then:

```bash
pip install -r requirements.txt
```

---

## Configuration

Copy:

```bash
copy .env.example .env
```

or on macOS/Linux:

```bash
cp .env.example .env
```

The application works without an LLM.

To enable an OpenAI-compatible LLM endpoint, configure:

```env
LLM_ENABLED=true
LLM_BASE_URL=https://api.openai.com/v1
LLM_API_KEY=your_api_key
LLM_MODEL=your_model_name
```

The LLM client uses a standard HTTP interface so the provider can be changed without rewriting the assistant architecture.

---

## Run

```bash
python -m app.main
```

The assistant will greet you and begin listening.

---

## Testing

Run:

```bash
python -m pytest
```

The tests intentionally focus on deterministic components so the routing and context layers can be validated without requiring a microphone or paid AI API.

---

## Example interaction

```text
Gouri: Hello. How can I help you?

You: What time is it?
Gouri: The current time is 05:30 PM.

You: Open YouTube.
Gouri: Opening YouTube.

You: Tell me a joke.
Gouri: [joke]

You: Explain artificial intelligence.
Gouri: [LLM response when configured]
```

---

## Engineering extensions

The architecture is intentionally designed for future additions such as:

- Weather API integration
- Calendar/task tools
- Retrieval-augmented generation
- Vector memory
- Wake-word detection
- FastAPI service layer
- Web dashboard
- Voice activity detection
- Speech model replacement
- Docker deployment
- Prometheus/OpenTelemetry instrumentation
- Persistent conversation storage
- Tool permission policies

These are intentionally not bundled as fake complexity. They can be added as measurable future iterations.

---

## Project evolution

### Original college version

```text
Microphone
    ↓
Google Speech Recognition
    ↓
if/elif keyword matching
    ↓
hard-coded response
    ↓
pyttsx3
```

### Re-engineered version

```text
Microphone
    ↓
Speech Recognition
    ↓
Intent Router
    ↓
Local Tool OR LLM
    ↓
Context + Observability
    ↓
Text-to-Speech
```

The project therefore demonstrates not only the original idea but also the ability to **revisit, refactor and productionize an early software prototype**.

---

## Resume positioning

Recommended project title:

**Gouri AI — Hybrid Voice Intelligence Assistant**

Suggested technology line:

**Python, Speech Recognition, NLP, LLM APIs, OOP, REST APIs, Automation, Testing, Logging**

Do not add performance percentages or accuracy numbers to a resume until they have been measured from the implemented version.

---

## License

Use this project as your own portfolio repository. Replace placeholder URLs and personalize the metadata before publishing.
