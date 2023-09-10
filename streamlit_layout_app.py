
# streamlit_layout_app.py

import streamlit as st
import random
import time
import openai
import pandas as pd
import pandasql as psql

# Access API key from Streamlit secrets and set key 
api_key = st.secrets["openai_api_key"]
openai.api_key = api_key

# Cache data to improve performance using Streamlit's caching mechanism
@st.cache_data
def load_data(path):
    # Read the CSV file at the given 'path' into a Pandas DataFrame
    df = pd.read_csv(path)
    return df

# Load movies, companies, and music data using the load_data function
# Cached data will be used after the first load
movies_df = load_data(llm_data/'movies.csv')  
companies_df = load_data('llm_data/webscrape.csv')  
music_df = load_data('llm_data/musicdata.csv')  

# Cache data transformation to improve performance
@st.cache_data
def company_rev_rename(companies_df):
    # Rename the 'Revenue (USD millions)' column to 'Revenue'
    companies_df.rename(columns={'Revenue (USD millions)': 'Revenue'}, inplace=True)
  return
company_rev_rename(companies_df)

@st.cache_data
def generate_dataframe_metadata(dataframe_dict):
    """
    Generate metadata string for dataframes in the dictionary.
    
    Parameters:
        dataframe_dict (dict): Dictionary of dataframe names and dataframes.
        
    Returns:
        str: Metadata string.
    """
    df_metadata = "" 
    
    # Loop through each dataframe in the dictionary
    for df_name, df in dataframe_dict.items():
        # Add dataframe name
        df_metadata += f"Dataframe: {df_name}\n"
        
        # Add column names and types
        df_metadata += "Column Names and Types:\n"
        for col, dtype in zip(df.columns, df.dtypes):
            df_metadata += f"  - {col}: {dtype}\n"
        
        # Add sample row format
        sample_row = df.iloc[0]
        df_metadata += "Sample Row Format (assume the data values are fake):\n"
        for col, value in sample_row.items():
            df_metadata += f"  - {col}: {type(value).__name__} ({value})\n"
        
        # Add a newline for readability
        df_metadata += "\n"
    
    return df_metadata  # Return the metadata string

# Create a dictionary of dataframes
dataframes = {'companies_df': companies_df, 'movies_df': movies_df, 'music_df': music_df}

# Generate and store metadata
metadata = generate_dataframe_metadata(dataframes)




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
    
    # Show 'Clear Chat History' button only if chat history is not empty
    if st.session_state.chat_history:
        if st.button('Clear Chat History'):
            # Clearing session state for chat_history
            st.session_state.chat_history = []
            # Rerun the app to reflect the changes immediately
            st.experimental_rerun()

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

    
   

# Run the app
if __name__ == '__main__':
    main()
