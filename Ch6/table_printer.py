tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    c_width = 0
    for row in list:
        p_list = []
        for str in row:
            if len(str) > c_width:
                c_width = len(str)
            p_list.append(str)
        for str in p_list:
            print(str.rjust(c_width))


printTable(tableData)