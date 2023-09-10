
# streamlit_layout_app.py

import streamlit as st
import random
import time

# Initialize Streamlit app
def main():
    # Initialize chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        
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
    
   
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input('Type your question here:'):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        #Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)
     
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response= ""
            response = "Response from model"  # Placeholder response
            for chunk in response.split():
                
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)   
            
        # Add assistant response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": full_response})

    
    # Cache clear button
    if st.button('Clear Chat History'):
    # Clearing session state for chat_history
        st.session_state.chat_history = []
    # Rerun the app to reflect the changes immediately
        st.experimental_rerun()


# Run the app
if __name__ == '__main__':
    main()
