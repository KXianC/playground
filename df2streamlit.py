import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title='Demo', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def create_df():
    np.random.seed(seed=1)
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 15)), columns=['A']+['abcdefgjjjjjjz'+ str(x) for x in range(14)])
    df = df.reset_index(drop=True)
    return df


def run_streamlit(df):
    st.title('Uber pickups in NYC')
    st.subheader('Number of pickups by hour')

    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?",
        ['ALL'] + df.columns.to_list(),
    )
 
    values = st.sidebar.slider(
        'Select a range of values',
        df.A.min(), df.A.max(), (df.A.min(), df.A.max()))


    height, width = 3000, 2000
    mask = df.A.between(values[0], values[1])
    if add_selectbox not in df.columns.to_list():
        result = df[mask]
        st.dataframe(result, use_container_width=True, height=height)
        # st.dataframe(result, hide_index=True, use_container_width=True, height=height)
        st.sidebar.write('Shape after filter:', result.shape)
    else:
        result = df[mask][add_selectbox]
        st.dataframe(result, use_container_width=True, height=height)
        # st.dataframe(result, hide_index=True, use_container_width=True, height=height)
        st.sidebar.write('Shape after filter:', result.shape)

def main():
    df = create_df()
    run_streamlit(df)


if __name__ == '__main__':
    main()
