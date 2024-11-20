def find_max(numbers):
    """Hàm tìm số lớn nhất trong danh sách."""
    if not numbers:
        return None  # Trả về None nếu danh sách rỗng

    max_number = numbers[0]  # Giả sử số đầu tiên là lớn nhất
    for num in numbers:
        if num > max_number:
            max_number = num  # Cập nhật nếu tìm thấy số lớn hơn

    return max_number


# Nhập danh sách từ người dùng
user_input = input("Nhập danh sách các số, cách nhau bởi dấu cách: ")

# Chuyển chuỗi nhập vào thành danh sách số
try:
    numbers = list(map(float, user_input.split()))  # Chuyển sang kiểu float
except ValueError:
    print("Vui lòng nhập các số hợp lệ!")
    exit()

# Gọi hàm và in kết quả
if numbers:
    max_value = find_max(numbers)
    print(f"Số lớn nhất trong danh sách là: {max_value}")
else:
    print("Danh sách rỗng, không thể tìm số lớn nhất.")
