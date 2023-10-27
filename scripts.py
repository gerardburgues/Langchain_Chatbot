def save_uploaded_file(uploaded_file, save_path):
    """Save uploaded file to a specified path."""
    try:
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        return True
    except Exception as e:
        st.write(f"Error saving file: {e}")
        return False