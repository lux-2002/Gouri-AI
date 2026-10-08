# Gouri-AI 🤖

### Modular Python AI Voice Assistant — Evolved from a College Project into a Production-Style AI Application

Gouri-AI is a modular voice assistant built with **Python**, designed to demonstrate how a simple college project can be evolved into a more maintainable, testable, and extensible AI application.

The project combines **speech recognition, intent classification, LLM-powered responses, contextual conversation handling, tool orchestration, logging, automated testing, and Docker support** within a clean layered architecture.

> **From a college prototype → to a structured AI engineering project.**

---

## 🚀 Why This Project?

Instead of treating the original voice assistant as a one-file college project, Gouri-AI was redesigned around software engineering principles:

* Modular architecture instead of tightly coupled code
* Intent-driven request routing
* LLM integration for intelligent responses
* Context management for conversations
* Extensible tool system for assistant actions
* Automated unit testing
* Structured logging and configuration
* Environment-based secret management
* Docker-ready application structure

This project demonstrates both **AI application development and software engineering fundamentals**.

---

## 🧠 What Can Gouri-AI Do?

| Capability              | Implementation                  |
| ----------------------- | ------------------------------- |
| 🎙️ Speech Input        | Speech recognition pipeline     |
| 🧠 Intent Understanding | Intent classification           |
| 💬 AI Responses         | LLM-powered response generation |
| 🗂️ Context             | Conversation context management |
| 🌐 Browser Actions      | Browser tool integration        |
| 🎵 Music                | Music-related assistant actions |
| 😂 Entertainment        | Joke generation/tool            |
| 💻 System Actions       | System-level assistant tools    |
| 📝 Logging              | Structured application logging  |
| 🧪 Testing              | Pytest-based test suite         |
| 🐳 Deployment           | Docker support                  |

---

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │     User Input      │
                    │   Voice / Text      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Speech Layer     │
                    │ Recognition / TTS   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      AI Layer       │
                    │ Intent Classification│
                    │ LLM Response Engine │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Core Assistant    │
                    │ Context + Routing   │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
             ┌─────────────┐       ┌─────────────┐
             │    Tools    │       │   Context   │
             │ Browser     │       │ Conversation│
             │ Music       │       │ Management  │
             │ System      │       └─────────────┘
             │ Jokes       │
             └─────────────┘
```

The architecture separates **AI reasoning, application orchestration, speech processing, tools, configuration, and utilities**, making the system easier to extend without rewriting the entire application.

---

## 🛠️ Tech Stack

**Language**

`Python`

**AI / Intelligence**

`LLM Integration` · `Intent Classification` · `Context Management`

**Voice**

`Speech Recognition` · `Text-to-Speech`

**Application Architecture**

`Modular Python` · `Layered Architecture` · `Tool-Based Design`

**Testing**

`Pytest`

**Engineering**

`Logging` · `Environment Configuration` · `Exception Handling`

**DevOps**

`Docker` · `Requirements Management`

---

## 📈 Project Evolution

### Original College Project

The original implementation was a basic Python voice assistant built around a simple procedural flow:

```text
Voice Input
     ↓
Command Detection
     ↓
Hard-coded Actions
     ↓
Voice Output
```

### Current Version

The project was redesigned into a more scalable architecture:

```text
User Input
    ↓
Speech / Input Layer
    ↓
Intent Classification
    ↓
Context + Routing
    ↓
LLM / Tool Selection
    ↓
Tool Execution
    ↓
Response Generation
    ↓
Voice Output
```

The goal was not simply to add more features, but to demonstrate **how an early-stage project can be refactored using production-oriented engineering practices**.

---

## 🔬 Engineering Highlights

### Modular Design

AI, speech, tools, configuration, and core orchestration are separated into independent modules.

### Intent-Based Routing

User requests are classified before being routed to the appropriate response or tool.

### LLM Integration

The assistant can use an LLM-backed response layer instead of relying entirely on hard-coded responses.

### Extensible Tool System

Assistant capabilities are represented as independent tools, allowing new functionality to be added without heavily modifying the core assistant.

### Testable Architecture

Core components are covered with automated tests to reduce regressions during development.

### Production-Oriented Configuration

Secrets and environment-specific configuration are separated from source code through environment variables.

### Container Ready

The project includes Docker support for reproducible application environments.

---

## 🧪 Testing

The project includes automated tests covering core components such as:

* Context management
* Intent classification
* Request routing
* Tool behavior

Run the test suite with:

```bash
pytest
```

---

## 🐳 Run with Docker

Build the image:

```bash
docker build -t gouri-ai .
```

Run the container:

```bash
docker run --env-file .env gouri-ai
```

For detailed development/setup instructions, see the project documentation.

---

## 🎯 What This Project Demonstrates

This project showcases practical experience across:

**AI Engineering**

* LLM application integration
* Intent classification
* Context-aware interactions
* AI-assisted response generation

**Software Engineering**

* Modular architecture
* Separation of concerns
* Exception handling
* Testing
* Logging
* Configuration management

**Developer Engineering**

* Git/GitHub
* Docker
* Dependency management
* Project documentation

---

## 🔗 Project

**GitHub:**
https://github.com/lux-2002/Gouri-AI

---

## 👩‍💻 About the Project

Gouri-AI started as a college project and was later revisited with a professional software-engineering mindset.

The focus of the upgrade was to demonstrate the ability to **understand an existing codebase, identify architectural limitations, refactor components, introduce engineering practices, and evolve a prototype into a structured AI application.**
