import streamlit as st
from crewai.flow import Flow, start, listen
from myflow.crews.prompt_crew.prompt_crew import PromptCrew

class MyFlow(Flow):
    @start()
    def generated_prompt(self, user_input):
        inputs = {"user_input": user_input}
        prompt = PromptCrew().crew().kickoff(inputs=inputs)
        return prompt

    @listen(generated_prompt)
    def save_prompt(self, prompt):
        with open("prompt.md", "w") as f:
            f.write(str(prompt))
        return prompt

def run_flow(user_input):
    flow = MyFlow()
    return flow.generated_prompt(user_input)

# Streamlit UI
st.title("AI-Powered Prompt Generator")
user_input = st.text_input("Enter your request:", "generate a prompt for a Python game")

if st.button("Generate Prompt"):
    with st.spinner("Generating..."):
        generated_prompt = run_flow(user_input)
        st.success("Prompt Generated!")
        st.text_area("Generated Prompt:", generated_prompt, height=200)
