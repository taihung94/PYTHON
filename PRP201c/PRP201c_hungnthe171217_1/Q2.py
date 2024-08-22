def main():
    try:
        with open("integers_data.txt","r") as file:
            contents = file.read()
            list_num = [int(i) for i in contents.split(" ")]
            str_even=""
            for i in list_num:
                if i%2 == 0:
                    str_even=str_even+str(i)+" "

            print(f"Content of the input file (integers_data.txt):\n{contents}")

    except FileNotFoundError:
        print('File integers_data.txt is not found.')
    file.close()

    with open("even_numbers.txt","w") as file2:
        file2.writelines(str_even.strip())
        print(f"Content of the output file (even_numbers.txt):\n{str_even.strip()}")


if __name__ == '__main__':
    main()