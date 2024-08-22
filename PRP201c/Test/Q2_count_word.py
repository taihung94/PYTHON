def count_word_occurrences(filename):
    """
    Đọc tệp văn bản, đếm số lần xuất hiện của mỗi từ và tìm từ xuất hiện nhiều nhất.

    Args:
      filename: Tên của tệp văn bản.

    Returns:
      Một tuple chứa:
        - Một dictionary với key là các từ và value là số lần xuất hiện.
        - Từ xuất hiện nhiều nhất.
        - Số lần xuất hiện của từ xuất hiện nhiều nhất.
    """

    word_counts = {}
    most_frequent_word = ''
    max_frequency = 0

    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().split()  # Chuyển về chữ thường và tách thành các từ
            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

                # Cập nhật từ xuất hiện nhiều nhất
                if word_counts[word] > max_frequency:
                    max_frequency = word_counts[word]
                    most_frequent_word = word

    return word_counts, most_frequent_word, max_frequency


if __name__ == "__main__":
    filename = 'data2.txt'
    word_counts, most_frequent_word, max_frequency = count_word_occurrences(filename)

    # Hiển thị kết quả
    for word, count in word_counts.items():
        print(f"{word}: {count}", end=", ")
    print(f"\nThe word with the most frequency is '{most_frequent_word}' which appears {max_frequency} times.")