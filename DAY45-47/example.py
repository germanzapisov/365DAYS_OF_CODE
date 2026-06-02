def cull(integers):
    lists = list(str(integers))
    count=0
    result=0
    result += int(lists[0])
    for _ in lists:
        if count < len(lists) - 1:
            count+=1
            result += int(lists[count])
        else:
            new_result = str(result)
            if len(new_result) > 1:
                main_result = int(new_result[0]) + int(new_result[1])
                print(main_result)
            else:
                break

integers = int(input("input: "))

cull(integers)

