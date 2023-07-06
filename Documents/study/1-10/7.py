def tempre(x,y,z):
    x = str(x)
    y = str(y)
    z = str(z)

    result = x + "時の" + y + "は" + z

    return result

if __name__ == "__main__":
    #文字列
    x = 12
    y = '気温'
    z = 22.4

    answer1 = tempre(x,y,z)
    print(answer1)
 