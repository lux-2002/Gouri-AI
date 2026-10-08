# Architecture Notes

## Responsibilities

### `speech`
Owns microphone input and text-to-speech output.

### `core`
Owns the assistant lifecycle, routing and conversation context.

### `tools`
Contains isolated actions that the assistant can execute.

### `ai`
Contains intent classification and optional LLM integration.

### `utils`
Contains cross-cutting concerns such as logging.

## Request lifecycle

1. Capture speech.
2. Convert speech to text.
3. Normalize the request.
4. Route deterministic intents locally.
5. If no local intent is recognized, optionally use the LLM.
6. Store the interaction in bounded conversation context.
7. Convert the final response to speech.
8. Log execution metadata.

## Why hybrid instead of LLM-only?

Local deterministic tools are cheaper, faster and more predictable for simple actions. LLM routing is useful when language is ambiguous or open-ended.

This separation also makes testing easier because deterministic behavior does not depend on an external model.
