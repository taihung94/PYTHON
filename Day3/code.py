class SieuNhan:
    so_thu_tu =1
    suc_manh =50
    def __init__(self,ten,vu_khi,color) :
        self.ten=ten
        self.vu_khi=vu_khi
        self.color=color
        
    def bien_hinh(self):
        print(self.ten,'tôi bị ngu')   
    def kt_color(self):
        return self.color=='Red'

    @staticmethod     
    def f():
        print("tôi bị điên")
    @classmethod
    def from_str(cls,s):
        lst=s.split('-')
        new_lst=[st.strip() for st in lst]
        ten, vu_khi,color=new_lst
        return cls(ten,vu_khi,color)
 

sieu_Nhan_A=SieuNhan("Sieu nhan Đỏ",'kiem','red')
sieu_Nhan_B=SieuNhan("Sieu nhan xanh",'bua','blue')



# gọi regular method dùng đối tượng tạo ra đề gọi
sieu_Nhan_A.bien_hinh()
#gọi staticmethod  2 cách
sieu_Nhan_A.f()
SieuNhan.f()
#gọi class method
infor_str ="vàng - súng - yellow"
sieu_nhan_C=SieuNhan.from_str(infor_str)


class SinhVien:
    so_luong_sinh_vien = 0

    def __init__(self, ten):
        self.ten = ten
        # Khi một đối tượng sinh viên được tạo ra, tăng số lượng sinh viên lên 1
        SinhVien.so_luong_sinh_vien += 1

    @classmethod
    def dem_so_luong(cls):
        return cls.so_luong_sinh_vien

# Tạo các đối tượng sinh viên
sinh_vien_A = SinhVien("John")
sinh_vien_B = SinhVien("Alice")
sinh_vien_C = SinhVien("Bob")

# Lấy số lượng sinh viên đã được tạo ra
print("Số lượng sinh viên:", SinhVien.dem_so_luong())  # Output: 3