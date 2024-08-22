def gcd(a, b):
  """
  Tìm ước chung lớn nhất (GCD) của hai số nguyên a và b sử dụng thuật toán Euclid.

  Args:
    a: Số nguyên đầu tiên.
    b: Số nguyên thứ hai.

  Returns:
    Ước chung lớn nhất của a và b.
  """
  while b:
    a, b = b, a % b
  return a

while True:
  try:
    num1 = int(input("Nhập số nguyên dương thứ nhất: "))
    if num1 > 0:
      break
    else:
      print("Số phải là số dương. Vui lòng nhập lại.")
  except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên dương.")

while True:
  try:
    num2 = int(input("Nhập số nguyên dương thứ hai: "))
    if num2 > 0:
      break
    else:
      print("Số phải là số dương. Vui lòng nhập lại.")
  except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên dương.")

result = gcd(num1, num2)
print(f"Ước chung lớn nhất của {num1} và {num2} là: {result}")