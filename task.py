import unittest

def Task_list(List):
    extra_list = []
    #checking if the list is multiple of 10
    if len(List) % 10 != 0:
        print("Put multiple of 10")
        
    #remove multiple of 2 and 3
    for i in range(len(List)):
        if List[i] % 2 == 0 or List[i] % 3 == 0:
            extra_list.append(List[i])
    Input_List = List
    for elem in extra_list:
        if elem in Input_List:
            Input_List.remove(elem)
    return(Input_List)

            
    
    
    


List = [12,1,2,3,4,5,6,7,8,9]
print(Task_list(List))

# TEST CASES

def testcase1():
        List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = Task_list(List)
        assert result == ([1,5,7])
        

testcase1()


