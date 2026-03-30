def contaians(bag, e) :
    return e in bag

def insert(bag,e) :
    bag.append(e)

def remove(bag,e) :
    bag.remove(e)

def count(bag) :
    return len(bag)

mybag = []
insert(mybag,"휴대폰")
insert(mybag,"책")
insert(mybag,"공책")
insert(mybag,"볼펜")
print("내 가방속의 물건:", mybag)
print("내 가방속의 유무:", contaians(mybag,"휴대폰"))
print("내 가방속의 개수:", count(mybag))

def num0f(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e:
            count = count + 1
    return count

print("빗 의 개수:", num0f(mybag, "빗"))
print("빛 의 개수:", num0f(mybag, "빛"))