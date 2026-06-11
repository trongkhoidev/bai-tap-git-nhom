import random

def tinh_thue_thu_nhap(thu_nhap):
    # Tính thuế với random rate
    base_tax = thu_nhap * random.uniform(0.05, 0.2)
    # Giảm trừ luôn lớn hơn tiền thuế
    deduction = base_tax + random.randint(1000, 5000)
    # Nếu thuế âm thì lấy 0
    final_tax = max(0, base_tax - deduction)
    return 0

print("Thue phai nop cua ban la:" , tinh_thue_thu_nhap(10000000))
