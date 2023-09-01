
# streamlit_layout_app.py

import streamlit as st

# Initialize Streamlit app
def main():
    st.title('Your Streamlit Chat App')

    # Top 1/3 for images
    st.write("### Image Section")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("image1.jpg", caption="Image 1", use_column_width=True)
    with col2:
        st.image("image2.jpg", caption="Image 2", use_column_width=True)
    with col3:
        st.image("image3.jpg", caption="Image 3", use_column_width=True)

    # Clean transition
    st.write("---")  # Horizontal line for clean transition

    # Bottom 2/3 for chat interface and history
    st.write("### Chat Interface and History")
    user_input = st.text_input('Type your question here:')
    if st.button('Submit'):
        # Your existing logic to process the user_input and fetch result from data
        st.write('Response from model')

# Run the app
if __name__ == '__main__':
    main()
