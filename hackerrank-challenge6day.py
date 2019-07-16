
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        string = input()
        even_list = []
        odd_list = []
        for x in range(0, len(string)):
            if x == 0 or x % 2 == 0:
                even_list.append(string[x])
            else:
                odd_list.append(string[x])
        seperator = ''
        # print(*even_list, " ", *odd_list)
        print(seperator.join(even_list), seperator.join(odd_list))

"""
Input 
T:2
1-String: hola 

 2- string: world

Output: hl oa
Output: wrd ol
(pares e impares de index)
"""
