def to_csv_text(array):
    for i in array:
        array[i].append("\n")
    print(array)





to_csv_text([[0, 1, 2, 3, 45], [10, 11, 12, 13, 14], [20, 21, 22, 23, 24],[30, 31, 32, 33, 34]])
"""
assert_equals(
        to_csv_text([
            [0, 1, 2, 3, 45],
            [10, 11, 12, 13, 14],
            [20, 21, 22, 23, 24],
            [30, 31, 32, 33, 34]
        ]),
        "0,1,2,3,45\n10,11,12,13,14\n20,21,22,23,24\n30,31,32,33,34",
    )
"""

"""
input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]

output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
"""
