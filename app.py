# Import required libraries
import os
import streamlit as st
from main import *
from scripts import *


def list_and_delete_files():
    """List the files in ./docs and provide an option to delete them."""
    st.write("### Uploaded Files")
    # List files in ./docs
    files = os.listdir("./docs")
    for file_name in files:
        # Display each file with a button to remove it
        col1, col2 = st.columns([3, 2])  # adjust as per your preference
        col1.write(file_name)
        if col2.button(f"Remove {file_name}"):
            try:
                os.remove(os.path.join("./docs", file_name))
                st.success(f"Removed {file_name}")
            except Exception as e:
                st.error(f"Error removing {file_name}: {e}")


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

    # List and delete files
    list_and_delete_files()

    # Simple chat interface
    st.write("### Chat Interface")
    if user_input := st.text_input("You: "):
        answer, chat_history = run_chat(user_input, chat_history)
        st.write(f"Bot: {answer}")


if __name__ == "__main__":
    main()
