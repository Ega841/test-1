# def heap_fest_foo() -> None:
#     num = 100
#     num_2 = num
#
#     print(f'num: id {id(num)} ')
#     print(f'num_2: id {id(num_2)} ')
#
# heap_fest_foo()

# def heap_fest_foo() -> None:
#     num = 100
#     num_2 = num
#
#     print(f'num: id {id(num)} ')
#     print(f'num_2: id {id(num_2)} ')
#     num += 1
#     print(f'num: id {id(num)}')
#
# heap_fest_foo()

# def heap_fest_foo() -> None:
#     lst_num = [100]
#     lst_num_2 = lst_num
#
#     print(f'num: id {id(lst_num)} ')
#     print(f'num_2: id {id(lst_num_2)} ')
#     lst_num.append(101)
#     print(f'num: id {id(lst_num)} ')
#     print(f'num_2: id {id(lst_num_2)} ')
#
# heap_fest_foo()

def heap_fest_foo() -> None:
    str_num = '100'
    str_num_2 = str_num

    print(f'num: id {id(str_num)} ')
    print(f'num_2: id {id(str_num_2)} ')
    str_num.add(101)
    print(f'num: id {id(str_num)} ')
    print(f'num_2: id {id(str_num_2)} ')

heap_fest_foo()
