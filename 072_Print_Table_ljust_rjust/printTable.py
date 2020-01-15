"""
Wyświetlanie tabeli z lity [[][][]].
"""

tableData = [['jabłka', 'śliwki', 'wisienki', 'banany'],
             ['harmonijka', 'saksofon', 'gitara', 'perkusja'],
             ['Łukasz', 'Piotr', 'Helena', 'Jimmy']]


def col_width(table):       # określa szerokość kolumn
    tmp = []
    colwidth = [0] * len(tableData)  # tworzy listę [0, 0, 0]. Tu przechowamy maxy
    a = 0
    for i in range(len(table)):
        for j in range(len(tableData[i])):      # wszystkie podlisty są tej samej długości
            tmp.append(len(tableData[i][j]))
        colwidth[i] = max(tmp[a:a+4])
        a += 4
    return colwidth


def print_table(table, colwidth):
    i = 0
    for j in range(4):
        s = table[i][j].rjust(colwidth) + ' ' + table[i+1][j].rjust(colwidth) + ' ' + table[i+2][j].rjust(colwidth)
        print(s)


m = col_width(tableData)
m = max(m)
print(m)
print_table(tableData, m)
