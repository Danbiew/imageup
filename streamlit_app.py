import streamlit as st
from PIL import Image

# 제목 표시
st.title("이미지 2배 확장 앱")

# 사용자로부터 이미지 파일 업로드 받기
uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 업로드된 이미지 열기
    image = Image.open(uploaded_file)
    
    # 원본 이미지 표시
    st.image(image, caption="원본 이미지", use_column_width=True)
    
    # 이미지 크기 2배로 늘리기
    width, height = image.size
    enlarged_image = image.resize((width * 2, height * 2))
    
    # 확장된 이미지 표시
    st.image(enlarged_image, caption="2배 확장된 이미지", use_column_width=True)
