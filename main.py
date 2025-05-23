import sys
import os
import asyncio
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from workflows.form_agent import create_form_agent
from services.form_filler import fill_sample_form

if __name__ == "__main__":
    agent = create_form_agent()

    # Plain dictionary input
    initial_state = {"address": "1600 Pennsylvania Avenue NW, Washington, DC"}

    final_state = agent.invoke(initial_state)
    print("Final State:", final_state)
    if "address_info" in final_state:
        asyncio.run(fill_sample_form(final_state["address_info"]))
