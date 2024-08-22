def simple_yield():

    print("Bắt đầu hàm.")

    yield 1

    print("Tiếp tục từ yield đầu tiên.")

    yield 2

    print("Tiếp tục từ yield thứ hai.")

gen = simple_yield()

print(next(gen))  # In ra: 1

print(next(gen))  # In ra: 2