import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("沼气学术会议")
st.sidebar.info(
    """
    中国沼气学会学术年会:     
    <http://www.biogaschina.com.cn>         
    能源系统与电气工程会议:       
    <https://www.ncsti.gov.cn>
    """
)

st.sidebar.title("友情链接")
st.sidebar.info(
    """
    国际沼气网: <http://www.biogasintel.com>       
    中国农业农村部: <http://www.moa.gov.cn>          
    香港可再生能源网: <https://re.emsd.gov.hk>

    """
)

st.title("基础计算")

# with st.expander("See source code"):
#     with st.echo():
#         m = leafmap.Map()
#         m.split_map(
#             left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
#         )
#         m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')
#
# m.to_streamlit(height=700)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# load_css('./assets/style.css')

st.title('沼气经济价值计算模块')

# st.text('请输入沼气原料重量：')
# weight = st.number_input('请输入沼气原料重量：')
# st.text('请输入原料单价：')
# price = st.number_input('请输入原料单价：')
# type = st.radio('原料类型:', ('干', '湿'))
# st.text('请输入损失因子：')
# discount_factor = st.number_input('请输入损失因子：')
#
# if st.button('计算'):
#     # h1 = float(h) / 100
#     # w = float(w)
#
#     total_price = weight*price*discount_factor
#     total_price = round(total_price, 2)
#     message = {total_price}
#
#
#     if type == '干':
#         message = total_price*0.88
#     elif type == '湿':
#         message = total_price*0.75
#     else:
#         message = total_price
#
#     st.text("")
#     st.write(message)


with st.form("calc"):
    weight = st.number_input("请输入沼气原料重量：",value=10)
    price = st.number_input("请输入原料单价：",value=10)
    type = st.radio('原料类型:', ('干', '湿'))
    discount_factor = st.number_input('请输入损失因子：')
    total_price = weight*price*discount_factor
    total_price = round(total_price, 2)
    message = {total_price}


    if type == '干':
        message = total_price*0.88
    elif type == '湿':
        message = total_price*0.75


    if st.form_submit_button("计算"):
        f"总价是{message}"