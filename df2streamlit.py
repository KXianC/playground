import numpy as np
import pandas as pd
import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go

import pandas as pd
import plotly.offline as offline
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.express as px
import plotly.graph_objs as go

np.random.seed(123)
st.set_page_config(page_title='GEAR Demo', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

def create_df():
    np.random.seed(seed=1)
    df = pd.DataFrame(np.random.randint(0, 100, size=(100, 15)), columns=['A']+['abcdefgjjjjjjz'+ str(x) for x in range(14)])
    df = df.reset_index(drop=True)
    return df



# def Bubble():       
#     df = px.data.gapminder()
    
#     fig = px.scatter(df.query("year==2007"), x="gdpPercap", y="lifeExp",
#               size="pop", color="continent",
#                      hover_name="country", log_x=True, size_max=60)
#     # Plot the data
#     st.plotly_chart(fig)
     
# def Scatter():
#     fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    
#     # Plot the data
#     st.plotly_chart(fig)
       
# def Line():
#     df = px.data.stocks()
#     fig = px.line(df, x='date', y="GOOG")
#     st.plotly_chart(fig)
   
# def aggregate_bar():
#     df = px.data.tips()
#     fig = px.histogram(df, x="sex", y="total_bill",
#                  color='smoker', barmode='group',
#                  histfunc='avg',
#                  height=400)
    
#     st.plotly_chart(fig)
   
# def bar_charts():
#     data_canada = px.data.gapminder().query("country == 'Canada'")
#     fig = px.bar(data_canada, x='year', y='pop')

#     st.plotly_chart(fig)
   
# def pie():
#     df = px.data.tips()
#     fig = px.pie(df, values='tip', names='day', color='day',
#                  color_discrete_map={
#  'Thur':'lightcyan',
#                                      'Fri':'cyan',
#                                      'Sat':'royalblue',
#                                      'Sun':'darkblue'})
#     st.plotly_chart(fig)
   
# def pulled_out():    
#     labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
#     values = [4500, 2500, 1053, 500]
    
#     # pull is given as a fraction of the pie radius
#     fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0.2, 0, 0])])   
#     st.plotly_chart(fig)

# def Layouts_plotly():
#     st.sidebar.write('导航栏')
#     add_selectbox = st.sidebar.radio(
#         "plotly基本图",
#         ("Bubble", "Scatter", "Line","aggregate_bar","bar_charts","pie","pulled_out")
#     )
#     if add_selectbox=="Bubble":
#         Bubble()
#     elif add_selectbox=="Scatter": 
#         Scatter() 
#     elif add_selectbox == "Line":
#         Line()
#     elif add_selectbox == "aggregate_bar":    
#         aggregate_bar()
#     elif add_selectbox == "bar_charts":    
#         bar_charts()
#     elif add_selectbox == "pie":     
#         pie()
#     elif add_selectbox == "pulled_out":
#         pulled_out()
#     # 补充表单
#     st.sidebar.button('基本数据表',on_click=Double_coordinates)


def run_streamlit():

    add_selectbox = st.sidebar.selectbox(
        "Select the client...",
        ['吴波', '李一名', '王伟', '陈晓东']
    )
    st.title(f'Client: {add_selectbox}')

    col1, col2, col3 = st.columns(3)
    col1.metric("持仓基金数", "3", "1")
    col2.metric("上月收益", "3%", "100,350 CNY")
    col3.metric("跑赢市场", "6%", "")



    a, b, c = ['1', '中国主题混合基金A', '1.15', '2022.03.01'], ['2', '一带一路主题基金B', '1.5', '2023.02.03'], ['3', '半导体主题基金C', '0.98', '2023.07.15']
    data = [a, b, c] 
    funds = pd.DataFrame(data, columns=['#', 'Name', '净值', '购入日期']) 

    st.subheader('已购买产品列表')
    st.dataframe(funds, hide_index=True)

    st.subheader('产品收益曲线')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=[a[1], b[1], c[1]])
    st.line_chart(chart_data)

    st.subheader('基于问卷的风险偏好类型')
    st.text('根据您最近填写的风险评估问卷, 您的风险偏好是: 保守稳健型')
    st.subheader('基于大模型的风险偏好类型')
    st.text('基于大模型分析, 你的风险偏好更倾向于: 积极进取型')

    from plotly.tools import FigureFactory as ff

    # Add histogram data
    x1 = np.random.randn(100) - 2
    x2 = np.random.randn(100)
    x3 = np.random.randn(1000) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['低风险', '中风险', '高风险']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('未来收益蒙特卡洛模拟')
    st.text('Plot the expected return curve under different situations. Scenario A, B, C, etc. ')
    st.image('test.png')

    st.subheader('客户提案')
    st.text('根据大模型分析结果和客户的期望, 帮助客户达到理想的风险组合')
    



    

def main():
    # df = create_df()
    run_streamlit()
    # Layouts_plotly()

if __name__ == '__main__':
    main()
