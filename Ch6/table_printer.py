tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    c_width = 0
    for row in list:
        for str in row:                             # find the longest word to correctly set column width
            if len(str) > c_width:
                c_width = len(str)
    for row in list:
        for i in range(len(row)):                   # gets number of items in each row
            c_list = []
            for j in range(len(list)):              # gets the number of inner lists
                c_list.append(list[j][i])           # pull appropriate string from each inner list
            for c in c_list:
                print(c.rjust(c_width), end=" ")    # prints item "i" from each inner list
            print("")
        break                                       # iterated through all items already


printTable(tableData)