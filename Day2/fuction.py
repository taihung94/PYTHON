# # packing args và unpacking
# def lf(*k,m='hung'):  #sau *k thì ko đc là position parameter mà phải là keywork
#     print(k[3],m)
# li=['123','hung','234','45']
# lf(*li)
# lf('123','hung','234','45')
#---------------------------------------------------
# # Positional-Only and Keyword-Only
# #  Positional-Only là a,b,c/ Keyword-Only là d
# def pos(a,b,c,d=8):
#     print(a,b,c,d)
# pos(1,2,3)
# pos(1,3,5,d=9)
# # các Keyword-Only parameter luôn ở cuối có thể dùng dấu * để phân cách
# def po2(a,b,c,*,d=8):
#     print(a,b,c,d)
# ----------------------------------------------------
# # lệnh yield in python
#  #không dùng yield phải tạo ra một list tạm là sq để lưu trữ
# def squa(lst):
#     sq=[]
#     for num in lst:
#         sq.append(num**2)
#     return sq
# for value in squa([1,2,3]):
#     print(value)
# print('Dùng yield-----------')
# def squa2(lst):
#     for num in lst:
#         yield lst
# for value in squa2([1,2,3]):
#     print(value)

# -------------------------------------------------

# Lambda in Python

hung = lambda x, y=9: x+y
print(hung(6))