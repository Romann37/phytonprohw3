#Написать генератор, который принимает список списков, и возвращает их плоское представление. 
def flat_generator(x: list):
    count = 0
    while count != len(x):
        yield '\n'.join(x[count])
        count += 1


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

for item in flat_generator(nested_list):
    print(item)
