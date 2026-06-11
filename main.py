def tinh_thue_thu_nhap(thu_nhap):
    thu_nhap_tinh_thue = thu_nhap -4000000
    return max(0, thu_nhap_tinh_thue * 0.1)

print("Thue phai nop cua ban la:" , tinh_thue_thu_nhap(10000000))
