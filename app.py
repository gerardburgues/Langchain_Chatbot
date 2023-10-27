# Import required libraries
import streamlit as st
from main import *
from scripts import *


def main():
    chat_history = []
    st.title("Multi-File Upload and Chat Interface")

    if uploaded_files := st.file_uploader("Choose files", accept_multiple_files=True):
        for file in uploaded_files:
            # Create docs directory if it doesn't exist
            if not os.path.exists("./docs"):
                os.makedirs("./docs")

            file_path = os.path.join("./docs", file.name)
            if save_uploaded_file(file, file_path):
                st.write(f"File {file.name} uploaded and saved to ./docs!")
            else:
                st.write(f"Failed to save {file.name}")

    # Simple chat interface
    st.write("### Chat Interface")
    if user_input := st.text_input("You: "):
        answer, chat_history = run_chat(user_input, chat_history)
        st.write(f"Bot: {answer}")


if __name__ == "__main__":
    main()
