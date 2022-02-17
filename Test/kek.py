if __name__ == '__main__':
    s = 'aab'
    list = []
    temps = s
    for i,item in enumerate(s):
        print(temps)

        temps = temps[1:]
        for b,item1 in enumerate(temps):
            if s[i]==temps[b]:
                split = temps.split(temps[b])
                list.append(len((split[0])))
                if b > 1:
                    list[len(list)-1]+=1
                break
    if list ==[]:
        list.append(len(s))
    list.sort(reverse=True)
    if list[0] == 0:
        list[0] =1
    print(list[0])