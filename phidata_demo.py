import os
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.deepseek import DeepSeekChat

os.environ['OPENAI_API_KEY'] = 'sk-YOUR_API_KEY'

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=DeepSeekChat(
        api_key=os.environ["OPENAI_API_KEY"],
        model_name="deepseek-coder"
    ),
    tools=[DuckDuckGo()],
    markdown=True,
    show_tool_calls=True,
)
web_agent.print_response("Whats happening in France?", stream=True)