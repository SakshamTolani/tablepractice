def isCorrect(table,number):
    c=0
    lst=[number*i for i in range(1,11)]
    for j in range(10):
        if lst[j]!=table[j]:
            print(f'This table is faulty at position {j}. It should be {lst[j]} in place of {table[j]}')
            c+=1
    if c==0:
        print(f'Table given by you is correct and needs no rectification!!')

if __name__=='__main__':
    l=[]
    for i in range(10):
       l.append(int(input('Enter numbers one by one you acquired: ')))
    number=int(input('Enter the number for which you want to check the table: '))
    isCorrect(l,number)