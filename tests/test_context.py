from app.core.context import ConversationContext


def test_context_is_bounded():
    context = ConversationContext(max_messages=2)

    context.add("user", "one")
    context.add("assistant", "two")
    context.add("user", "three")

    messages = context.messages()

    assert len(messages) == 2
    assert messages[0]["content"] == "two"
    assert messages[1]["content"] == "three"


def test_context_clear():
    context = ConversationContext(max_messages=3)
    context.add("user", "hello")

    context.clear()

    assert len(context) == 0
