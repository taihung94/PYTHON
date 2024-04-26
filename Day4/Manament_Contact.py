# kiểm tra điều kiện của biến
class Check_Conditions:
    # kiểm tra giá trị int nhập vào của người dùng hợp lệ và lớn hơn min nhở hơn max
    @staticmethod
    def check_input_int_limit(min_value, max_value):
    # Loop until user input is correct
        while True:
            try:
                user_input = int(input().strip())
                if user_input < min_value or user_input > max_value:
                    raise ValueError
                return user_input
            except ValueError:
                print("Please input a number in the range [{}, {}]".format(min_value, max_value))
                print("Enter again: ", end="")
        # kiểm tra str nhập vào là hợp lệ không phải xâu rỗng
    @staticmethod
    def check_input_str():
        while True:
            try:
                user_input=input().strip()
                if len(user_input)==0:
                    raise Exception
                return user_input
            except Exception:
                print('Not empty string. Please input again: ')   
    @staticmethod
    def check_phone():
        while True:
            try:
                user_input=input().strip()
                if len(user_input)==0 or len(user_input)!=10 or user_input[0]!='0':
                    raise Exception                    
                if user_input.isdigit==False:
                    raise Exception  
                return user_input      
            except Exception:
                print('Wrong format phone number. Please input again: ')


# # Tạo đối tượng

class Contact:
    so_thu_tu =1
    def __init__(self,group,address,phone,first_name,last_name): 
      self.group=group
      self.address=address
      self.phone=phone
      self.first_name=first_name
      self.last_name=last_name
      self.id=Contact.so_thu_tu
      Contact.so_thu_tu+=1


    def display(self):
        print("{:<5}{:<20}{:<20}{:<20}{:<5}{:<20}".format(
            self.id,
            self.first_name + " " + self.last_name,
            self.first_name,
            self.last_name,
            self.group,
            self.address,
            self.phone
        ))

# hung =Contact(12345,2,3,'Nguyễn','Hưng')
# mai =Contact(1,2,3,'Nguyễn','mai')
# hung.display()
# mai.display()

# # # Tạo class quản lý
# # class Manager:
# #     pass