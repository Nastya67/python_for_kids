import re
from .task_test import test


def check_res(fname, res):
    f = open(fname, 'r')
    txt = f.read().strip()
    f.close()
    if not txt == res:
        print("!", txt, "!")
        return False
    return True


def utest1():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    if not re.match(r"print\(\s*[\"\']Hello World![\"\']\s*\)", txt):
        return False
    if not check_res("out.txt", "Hello World!"):
        return False
    return check_res("err.txt", "")


def utest2():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    if not re.match(r"print\(\s*1.11\s*\*\s*70\s*\)", txt):
        return False
    if not check_res("out.txt", "77.7"):
        return False
    return check_res("err.txt", "")


def utest3():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    txt2 = txt + "\nprint(luck, type(luck))"
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt3 = "\n".join(["luck = 0"] + txt3[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    if not check_res("out.txt", "777"):
        return False
    if res2 != "777\n777 <class 'int'>":
        return False
    if res3 != "0":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest4():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join([strs[0]] + ["print(luck, type(luck))"] + [strs[2]] + ["print(luck, type(luck))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["luck = 0"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    txt4 = "\n".join(["luck = 0"] + strs[1:])
    res4, err4 = test(txt4, "tmp4", "out4", "err4")
    if not check_res("out.txt", "13\n77"):
        return False
    if res2 != "13 <class 'int'>\n77 <class 'int'>":
        return False
    if res3 != "0":
        return False
    if res4 != "0\n77":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "") and (err4 == "")


def utest5():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(triangles, circles, squares)"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(strs[:-1] + ["squares = 0"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    strs4 = [t if not t.startswith("triangles") else "triangles = 6" for t in strs]
    txt4 = "\n".join(strs4[:])
    res4, err4 = test(txt4, "tmp4", "out4", "err4")
    if not check_res("out.txt", "26"):
        return False
    if res2 != "7 14 5":
        return False
    if res3 != "21":
        return False
    if res4 != "23":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "") and (err4 == "")


def utest6():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(hello_string, type(hello_string))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["hello_string = 0"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    if not check_res("out.txt", "Hello World!"):
        return False
    if res2 != "Hello World! <class 'str'>":
        return False
    if res3 != "0":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest7():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(history, type(history))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["history = 0"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """She asks, "Can I take your pen, isn't it?"."""
    if not check_res("out.txt", answ):
        return False
    if res2 != answ+" <class 'str'>":
        return False
    if res3 != "0":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest8():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(template, name, grade)"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(strs[:-1] + ["name = 'a'", "grade='B'"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """%s wants to have a grade %s."""
    if not check_res("out.txt", answ % ("Nastya", "A")):
        return False
    if res2 != answ+" Nastya A":
        return False
    if res3 != answ % ("a", "B"):
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest9():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(LoL)"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["LoL = 'a'"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """LoL"""
    if not check_res("out.txt", answ*10):
        return False
    if res2 != answ:
        return False
    if res3 != "a"*10:
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest10():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(subjects, type(subjects))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["subjects = []"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """['Math', 'Music', 'literature', 'biology']"""
    if not check_res("out.txt", answ):
        return False
    if res2 != answ+" <class 'list'>":
        return False
    if res3 != "[]":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest11():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(subjects, type(subjects))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["subjects = [0, 1, 2, 3, 4, 5]"] + strs[1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    txt4 = "\n".join(strs[:1] + ["print(subjects)"])
    res4, err4 = test(txt4, "tmp3", "out3", "err3")
    answ = """['Math', 'Music', 'Literature', 'Chemistry']"""
    answ2 = """['Math', 'Music', 'Literature', 'Biology']"""
    if not check_res("out.txt", answ2):
        return False
    if res2 != answ2+" <class 'list'>":
        return False
    if res3 != "[0, 1, 2, 'Biology', 4, 5]":
        return False
    if res4 != answ:
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "") and (err4 == "")


def utest12():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(fruits, type(fruits))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["fruits = [0, 1, 2, 3, 4, 5]"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """['apples', 'pears', 'plums', 'apricots']"""
    answ2 = """['pears', 'plums']"""
    if not check_res("out.txt", answ2):
        return False
    if res2 != answ+" <class 'list'>":
        return False
    if res3 != "[1, 2]":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest13():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(quirk, type(quirk))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["quirk = [0]"] + strs[-1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    answ = """[1, 'two', [3, 'four']]"""
    if not check_res("out.txt", answ):
        return False
    if res2 != answ+" <class 'list'>":
        return False
    if res3 != "[0]":
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "")


def utest14():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(planets, type(planets))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["planets = [0]"] + strs[1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    txt4 = "\n".join(strs[:1] + ["print(planets)"])
    res4, err4 = test(txt4, "tmp3", "out3", "err3")
    answ = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if not check_res("out.txt", str(answ+["Pluto"])):
        return False
    if res2 != str(answ+["Pluto"])+" <class 'list'>":
        return False
    if res3 != "[0, 'Pluto']":
        return False
    if res4 != str(answ):
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "") and (err4 == "")


def utest15():
    f = open("tmp.py", 'r')
    txt = f.read().strip()
    f.close()
    strs = [x.strip() for x in txt.strip().split("\n") if x != ""]
    txt2 = "\n".join(strs[:-1] + ["print(planets, type(planets))"])
    res2, err2 = test(txt2, "tmp2", "out2", "err2")
    txt3 = "\n".join(["planets = [0]"] + strs[1:])
    res3, err3 = test(txt3, "tmp3", "out3", "err3")
    txt4 = "\n".join(strs[:1] + ["print(planets)"])
    res4, err4 = test(txt4, "tmp3", "out3", "err3")
    answ = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    if not check_res("out.txt", str(answ+["Pluto"])):
        return False
    if res2 != str(answ+["Pluto"])+" <class 'list'>":
        return False
    if res3 != "[0, 'Pluto']":
        return False
    if res4 != str(answ):
        return False
    return check_res("err.txt", "") and (err2 == "") and (err3 == "") and (err4 == "")


def utest16():
    pass

def utest17():
    pass

def utest18():
    pass

def utest19():
    pass


route = {1: utest1, 2: utest2, 3: utest3, 4: utest4, 5: utest5, 6: utest6, 7: utest7, 8: utest8, 9: utest9,
         10:utest10,11:utest11,12:utest12,13:utest13,14:utest14,15:utest15,16:utest16,17:utest17,18:utest18,19:utest19}
