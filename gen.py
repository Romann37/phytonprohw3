#Написать генератор, который принимает список списков, и возвращает их плоское представление. 
def flat_generator(x: list):
    count = 0
    x = [item for i in x for item in i]
    while count != len(x):
        yield x[count]
        count += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 5, 'i']
]

for item in flat_generator(nested_list):
    print(item)
