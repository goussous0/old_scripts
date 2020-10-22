# user = usr_name[0]
# name = usr_name[1]
# user = user[0].upper() + user[1:]
# name = name[0].upper() + name[1:]
# res = user + " " + name






def solve(s):
    res = ""
    chars = list(s)
    #usr_name = s.split()
    #for item in usr_name:
    #    word = item
    #    word = word[0].upper() + word[1:]
    #    if usr_name[0]==item:
     #       res += word
     #   else:
     #       res += " "+word
    tmp_char = ""
    for item in chars:
        if tmp_char== " ":
            item = item.upper()
            res += item
        elif item == chars[0]:
            res = item.upper()
        else:
            res += item

        tmp_char = item

    return res


if __name__ == '__main__':


    s = input()

    result = solve(s)

    print (result)
