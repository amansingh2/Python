
def func() -> None:
    ls1 = [1 , 3 , 5 ,7]
    ls2 = [2 , 4 , 6 ,8]
    ls3 = [11 , 12 , 13  ,14]

    res = [
        ele1*ele2*ele3 for ele1 in ls1 for ele2 in ls2 for ele3 in ls3
    ]
    print(len(res))

    print(res)






if __name__ == "__main__":
    func()