
# streamlit_layout_app.py

import streamlit as st

# Initialize Streamlit app
def main():
    st.title('Your Streamlit Chat App')

    # Top 1/3 for images
    st.write("### Image Section")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("Romantisized golden era movie theater screen from a side angle lights dimmed.jfif", caption="Movies", use_column_width=True)
    with col2:
        st.image("Corporate buildings in Manhattan from below looking up_.jfif", caption="Corporations", use_column_width=True)
    with col3:
        st.image("wide eyed lens shot vinyl record player in focus in the foreground background is a coffee shop but blurred with intense bokeh (1).jfif", caption="Music", use_column_width=True)

    # Clean transition
    st.write("---")  # Horizontal line for clean transition

    # Bottom 2/3 for chat interface and history
    st.write("### Chat Interface and History")
    
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # User input
    user_input = st.text_input('Type your question here:')

    # Add user input to chat history and display it
    if st.button('Submit'):
        st.session_state.chat_history.append({"type": "user", "message": user_input})
        
        # Logic to generate a response can go here
        response = "Response from model"  # Placeholder response
        st.session_state.chat_history.append({"type": "bot", "message": response})

    # Display chat history
    st.write("### Chat History")
    for chat in reversed(st.session_state.chat_history):
        if chat["type"] == "user":
            st.write(f'<div style="text-align: right; border-radius: 15px; background-color: lightblue; padding: 10px; margin: 10px;">{chat["message"]}</div>', unsafe_allow_html=True)
        else:
            st.write(f'<div style="text-align: left; border-radius: 15px; background-color: #A1E887; padding: 10px; margin: 10px;">{chat["message"]}</div>', unsafe_allow_html=True)


# Run the app
if __name__ == '__main__':
    main()
