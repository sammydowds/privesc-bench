from inspect_ai.agent import Agent, agent, react
from inspect_ai.tool import bash, python
from inspect_ai.model import CompactionAuto
from prompts import PRIVESC_PROMPT

# Compaction Docs
# https://inspect.aisi.org.uk/compaction.html#overview


@agent
def privesc_agent() -> Agent:
    """Base ReAct agent for researching privilege escelation."""

    return react(
        name="Privilege Escelation Agent",
        description="An agent to research escelating privilege on linux systems.",
        prompt=PRIVESC_PROMPT,
        tools=[bash(user="www-data"), python(user="www-data")],
        compaction=CompactionAuto(),
    )
