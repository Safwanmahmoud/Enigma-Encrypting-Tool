from collections import deque
from tkinter import *
from tkinter import ttk
# import pyperclip

# Inserting the 3 Rotors
global rot1, rot2, rot3

rot1 = [["a", "s", "q", "a"], ["b", "q", "o", "b"], ["c", "d", "v", "c"], ["d", "f", "c", "d"], ["e", "h", "i", "e"],
        ["f", "j", "d", "f"], ["g", "l", "r", "g"], ["h", "n", "e", "h"], ["i", "e", "u", "i"], ["j", "r", "f", "j"],
        ["k", "t", "s", "k"], ["l", "v", "g", "l"], ["m", "z", "w", "m"], ["n", "x", "h", "n"], ["o", "b", "x", "o"],
        ["p", "p", "p", "p"], ["q", "a", "b", "q"], ["r", "g", "j", "r"], ["s", "k", "a", "s"], ["t", "y", "k", "t"],
        ["u", "i", "z", "u"], ["v", "c", "l", "v"], ["w", "m", "y", "w"], ["x", "o", "n", "x"], ["y", "w", "t", "y"],
        ["z", "u", "m", "z"]]
rot2 = [["w", "a", "z"], ["l", "b", "d"], ["i", "c", "i"], ["b", "d", "n"], ["r", "e", "j"], ["f", "f", "f"],
        ["v", "g", "v"], ["o", "h", "t"], ["c", "i", "c"], ["e", "j", "w"], ["n", "k", "m"], ["u", "l", "b"],
        ["k", "m", "x"], ["d", "n", "k"], ["t", "o", "h"], ["p", "p", "p"], ["y", "q", "y"], ["s", "r", "e"],
        ["z", "s", "r"], ["h", "t", "o"], ["x", "u", "l"], ["g", "v", "g"], ["j", "w", "a"], ["m", "x", "u"],
        ["q", "y", "q"], ["a", "z", "s"]]
rot3 = [["q", "a", "q"], ["e", "b", "s"], ["k", "c", "v"], ["f", "d", "t"], ["n", "e", "b"], ["p", "f", "d"],
        ["y", "g", "k"], ["o", "h", "y"], ["l", "i", "o"], ["j", "j", "j"], ["g", "k", "c"], ["r", "l", "i"],
        ["z", "m", "z"], ["s", "n", "e"], ["i", "o", "h"], ["t", "p", "f"], ["a", "q", "a"], ["v", "r", "l"],
        ["b", "s", "n"], ["d", "t", "p"], ["w", "u", "x"], ["c", "v", "r"], ["x", "w", "u"], ["u", "x", "w"],
        ["h", "y", "g"], ["m", "z", "m"]]


def walk(ro1, ro2, ro3, ltr):
    ref = [9, 24, 21, 8, 6, 5, 26, 4, 1, 15, 13, 20, 11, 17, 10, 23, 14, 19, 18, 12, 3, 25, 16, 2, 22, 7]
    check = True
    # step 1
    for x in range(26):
        if ltr == ro1[x][0]:
            s1 = x
            check = False
    if check:
        return ltr

    # step 2
    s2 = ro1[s1][1]

    # step 3
    for x in range(26):
        if s2 == ro1[x][3]:
            s3 = x

    # step 4
    s4 = ro2[s3][0]

    # step 5
    for x in range(26):
        if s4 == ro2[x][1]:
            s5 = x

    # step 6
    s6 = ro3[s5][0]

    # step 7
    for x in range(26):
        if s6 == ro3[x][1]:
            s7 = x

    # step 8
    s8 = ref[s7] - 1

    # step 9
    s9 = ro3[s8][2]

    # step 10
    for x in range(26):
        if s9 == ro3[x][1]:
            s10 = x

    # step 11
    s11 = ro2[s10][2]

    # step 12
    for x in range(26):
        if s11 == ro2[x][1]:
            s12 = x

    # step 13
    result = ro1[s12][2]

    return result


def rotate(arr):
    d = deque(arr)
    d.rotate(1)
    d = list(d)
    return d


root = Tk()
root.title("ENIGMA")

# labels:
ttk.Label(root, text="INPUT").grid(row=0, column=4, padx=10, pady=10, columnspan=1)
ttk.Label(root, text="OUTPUT").grid(row=3, column=4, padx=10, pady=10, columnspan=1)

# Texts
msg = Text(root, width=60, height=5, font=('Arial', 16))
msg.grid(row=2, column=1, columnspan=7, padx=20, pady=10)
cmsg = Text(root, width=60, height=5, font=('Arial', 16))
cmsg.grid(row=4, column=1, columnspan=7, padx=20, pady=10)

# Rotors
rotor1 = StringVar(root)
rotor2 = StringVar(root)
rotor3 = StringVar(root)

rotor1.set("a")  # default value
rotor2.set("a")  # default value
rotor3.set("a")  # default value

r1 = OptionMenu(root, rotor1, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z").grid(row=7, column=3, columnspan=1, padx=10, pady=20)
r2 = OptionMenu(root, rotor2, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z").grid(row=7, column=4, columnspan=1, padx=10, pady=20)
r3 = OptionMenu(root, rotor3, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                "s", "t", "u", "v", "w", "x", "y", "z").grid(row=7, column=5, columnspan=1, padx=10, pady=20)


# Functions
def setting():
    # rotor 1
    global rot1, rot2, rot3
    for x in range(26):
        if rot1[0][0] == rotor1.get():
            break
        else:
            rot1 = rotate(rot1)
    # rotor 2
    for x in range(26):
        if rot2[0][1] == rotor2.get():
            break
        else:
            rot2 = rotate(rot2)

    # rotor 3
    for x in range(26):
        if rot3[0][1] == rotor3.get():
            break
        else:
            rot3 = rotate(rot3)


def enc():
    global rot1, rot2, rot3
    inp = msg.get(1.0, "end-1c")
    n = len(inp)
    counter = 0
    incmsg = []
    while True:
        for x in range(26):
            for x in range(26):
                ltr = inp[counter]
                incmsg.append(walk(rot1, rot2, rot3, ltr))
                counter += 1
                rot1 = rotate(rot1)
                rotor1 = rot1[0][0]
                if counter == n:
                    break
            rot2 = rotate(rot2)
            rotor2 = rot2[0][1]
            if counter == n:
                break
        rot3 = rotate(rot3)
        rotor3 = rot3[0][1]
        if counter == n:
            break

    incmsg = ''.join(incmsg)
    cmsg.delete(1.0, 'end')
    cmsg.insert(END, incmsg)


def copy():
    pyperclip.copy(cmsg.get(1.0, "end-1c"))


# Buttons
enc = ttk.Button(root, text="Encrypt/decrypt", command=enc).grid(row=9, column=4, columnspan=3, padx=10, pady=20)
cop = ttk.Button(root, text="copy", command=copy).grid(row=9, column=6, columnspan=2, padx=10, pady=20)
setting = ttk.Button(root, text="set", command=setting).grid(row=8, column=4, columnspan=1, padx=10, pady=20)

root.mainloop()
