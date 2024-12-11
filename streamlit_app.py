import streamlit as st
from PIL import Image
import numpy as np
from io import BytesIO  # 이 부분을 추가했습니다

def resize_image(image, scale_factor=2):
    """
    Resize the image by a given scale factor using PIL
    
    :param image: PIL Image object
    :param scale_factor: Factor by which to multiply image dimensions
    :return: Resized PIL Image object
    """
    # Get original image dimensions
    width, height = image.size
    
    # Calculate new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    
    # Resize the image using LANCZOS (high-quality resampling)
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    
    return resized_image

def main():
    st.title("🖼️ Image Resizer")
    
    # Sidebar for configuration
    st.sidebar.header("Image Resize Settings")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image", 
        type=['png', 'jpeg', 'jpg', 'webp', 'bmp', 'tiff']
    )
    
    # Resize factor selection
    resize_option = st.sidebar.selectbox(
        "Resize Factor", 
        options=[2, 3, 4, 5],
        index=0
    )
    
    # Process and display image if uploaded
    if uploaded_file is not None:
        # Read the image
        original_image = Image.open(uploaded_file)
        
        # Display original image info
        st.sidebar.write("Original Image Dimensions:")
        st.sidebar.write(f"Width: {original_image.size[0]} px")
        st.sidebar.write(f"Height: {original_image.size[1]} px")
        
        # Resize the image
        resized_image = resize_image(original_image, scale_factor=resize_option)
        
        # Display resized image info
        st.sidebar.write("\nResized Image Dimensions:")
        st.sidebar.write(f"Width: {resized_image.size[0]} px")
        st.sidebar.write(f"Height: {resized_image.size[1]} px")
        
        # Create columns for display
        col1, col2 = st.columns(2)
        
        # Display original image
        with col1:
            st.subheader("Original Image")
            st.image(original_image, use_container_width=True)
        
        # Display resized image
        with col2:
            st.subheader(f"Resized Image (x{resize_option})")
            st.image(resized_image, use_container_width=True)
        
        # Download button for resized image
        buffered = BytesIO()
        resized_image.save(buffered, format=original_image.format)
        resized_byte_im = buffered.getvalue()
        
        st.download_button(
            label="Download Resized Image",
            data=resized_byte_im,
            file_name=f"resized_image.{original_image.format.lower()}",
            mime=f"image/{original_image.format.lower()}"
        )

if __name__ == "__main__":
    main()
