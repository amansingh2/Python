
def func() -> None:
    ls1 = [1 , 3 , 5 ,7]
    ls2 = [2 , 4 , 6 ,8]
    ls3 = [11 , 12 , 13  ,14]

    res = [
        ele1*ele2*ele3 for ele1 in ls1 for ele2 in ls2 for ele3 in ls3
    ]

    # d = {}
    # d["1"] = 2
    # d["4"] = 8
    d = {"a": 2, "b": 8}
    # print(**d)

    print(*d.items())
    print(*d.values())
    # print(**d)
    print(len(res))

    print(" ".join(f"{k} = {v}" for k , v in d.items()))

    # print(res)






if __name__ == "__main__":
    func()