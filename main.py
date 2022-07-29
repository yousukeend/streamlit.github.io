import streamlit as st
import time

st.title('Streamlit 入門してみた')

st.write('バー表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!'

left_column, right_coulumn = st.beta_columns(2)
button = left_column.button('右からカラムに文字を表示')
if button:
  right_coulumn.write('ここは右からむ')

expander = st.beta_expander('問い合わせ')
expander.write('お問合せをする')
# if st.checkbox('Show Image'):
#   img = Image.open('001.jpg')
#   st.image(img, caption='yosuke', use_column_width=True)

# text = st.text_input('趣味は何')
# condition = st.slider('今日の調子はどうですか', 0, 100, 50)
# 'あなたの趣味は、', text, 'です'

# '調子は:', condition



