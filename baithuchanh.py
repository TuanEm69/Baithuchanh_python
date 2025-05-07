import requests

# Thông tin cần thiết
access_token = 'EAA7ZCJZAoYOrIBOzdLzrkJLHkEhURDVLbC5ZA6lnjjcrEMATRHpHZAcnU5CBUMcZBuBBcpJfVkSUv4igP15eywTduyfKAsNb3Fv6lhvx7d5KP24adeGcoQ1vOiYDjSRdxBBXg8NnrU8MCEG95DwlrBZAabWhRkPVr9c4vozLT8OblPBLViy3o37XjXO6DATtigyFlmDlZAYkOksh2qVfRJ9dRnr'  # Thay bằng access token của bạn
page_id = '641158665753697'            # Thay bằng ID của trang bạn quản lý
message = 'Đây là bài viết tự động từ Python của Tuấn AnhAnh 🚀'  # Nội dung bài đăng

# URL API của Facebook để đăng bài
url = f'https://graph.facebook.com/{page_id}/feed'

# Dữ liệu gửi đi
payload = {
    'message': message,
    'access_token': access_token
}

# Gửi yêu cầu POST đến Facebook Graph API
response = requests.post(url, data=payload)

# Xử lý kết quả
if response.status_code == 200:
    print("✅ Đăng bài thành công!")
    print("ID bài viết:", response.json().get('id'))
else:
    print("❌ Lỗi khi đăng bài:")
    print(response.status_code)
    print(response.text)