from List import List

if __name__ == '__main__':

    list = List([
        [["bap"], ["nya"]],
        [[7.7, 0.2, -4.5], [5, 0, 3]],
        [[["inside"]], [1], [2.8]]
    ])

    print(list[0,0,0])
    print(list[2,0,0])
    print(list[1,1,1])
    print(list[2,2,0])
