def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for i in range(len(elements)):
            min_index = i
            for j in range(min_index + 1, len(elements)):
                if elements[j][sort_by] < elements[min_index][sort_by]:
                    min_index = j
            if i != min_index:
                elements[i], elements[min_index] = elements[min_index], elements[i]

if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Raj', 'Last Name': 'Sharma'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Jaya', 'Last Name': 'Seth'},
        {'First Name': 'Armaan', 'Last Name': 'Dadra'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    multilevel_selection_sort(
        elements, ['First Name', 'Last Name'])
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')