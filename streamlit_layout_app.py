
# streamlit_layout_app.py

import streamlit as st
import random
import time

# Initialize Streamlit app
def main():
    st.title('Multi-Domain Tabular Data Chat App')

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

    
    # Cache clear button
    if st.button('Clear Chat History'):
    # Clearing session state for chat_history
        st.session_state.chat_history = []
    # Rerun the app to reflect the changes immediately
        st.experimental_rerun()
   

   # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # chat interface
    st.write("### Chat Interface")
    user_input = st.chat_input('Type your question here:')

    # Add user input to chat history and display it
    if st.button('Submit'):
        st.session_state.chat_history.append({"type": "user", "message": user_input})

    
 
    
  
   # Display chat history using st.chat_message
    st.write("### Chat History")

    for chat in reversed(st.session_state.chat_history):
        if chat["type"] == "user":
            st.chat_message(chat["message"], user_type='user')
        else:
            st.chat_message(chat["message"], user_type='assistant')


    

    
   # Logic to generate a response can go here
    response = "Response from model"  # Placeholder response
    st.session_state.chat_history.append({"type": "bot", "message": response})
    
   

  

# Run the app
if __name__ == '__main__':
    main()
