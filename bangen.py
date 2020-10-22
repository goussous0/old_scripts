def ban_gen(x, y):
    ## code goes here
    banner_lst = []
    midx = int((int(x / 2) + 1))
    midy = int((y / 2 + 1))
    line = ""
    sym = ".|."
    mid_line = ""
    for i in range(1, x + 1):
        # print (i)
        if i == midx:
            mid_line = "WELCOME".center(y, "-")
            # banner_lst.append(line)
            # print (line)
        elif i < midx:
            line = str(sym * ((i * 2) - 1)).center(y, "-")
            banner_lst.append(line)
            # print (line)
    tmp_lst = banner_lst[::-1]

    for item in banner_lst:
        print(item)
    print(mid_line)
    for item in tmp_lst:
        print(item)


if __name__ == "__main__":
    nums = input().split()
    x, y = int(nums[0]), int(nums[1])
    ban_gen(x, y)
