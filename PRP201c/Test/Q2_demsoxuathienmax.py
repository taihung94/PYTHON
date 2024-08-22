def count_occurrences(filename="data.txt"):
  """Đếm số lần xuất hiện của mỗi số trong file và in ra số xuất hiện nhiều nhất.

  Args:
    filename: Tên file cần đọc dữ liệu, mặc định là "data.txt".
  """
  try:
    with open(filename, 'r') as file:
      numbers = [int(num) for num in file.read().split(',')]
  except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy file '{filename}'")
    return

  counts = {}
  for number in numbers:
    if number in counts:
      counts[number] += 1
    else:
      counts[number] = 1

  print("Số lần xuất hiện của các số:")
  for number, count in counts.items():
    print(f"Số {number}: {count} lần")

  max_count = max(counts.values())
  most_frequent_numbers = [number for number, count in counts.items() if count == max_count]

  print("\nSố xuất hiện nhiều nhất:")
  if len(most_frequent_numbers) == 1:
    print(f"Số {most_frequent_numbers[0]} xuất hiện nhiều nhất: {max_count} lần")
  else:
    print(f"Các số {', '.join(map(str, most_frequent_numbers))} cùng xuất hiện nhiều nhất: {max_count} lần")


# Chạy chương trình
count_occurrences() 