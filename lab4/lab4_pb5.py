from collections import Counter
def count_elements(lst):
    count = Counter(lst)
    for key, value in count.items():
        print(key, "=>", value)

sample_list = [10, 20, 30, 30, 30, 30, 20, 40]
count_elements(sample_list)