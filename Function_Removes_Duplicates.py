def remove_duplicates(List):
    New_List =[]

    for i in List:
        if i not in New_List:
            New_List.append(i)

    return New_List

numbers=[1,5,9,8,2,1,7,6,3,6,2,9,5]

print(remove_duplicates(numbers))