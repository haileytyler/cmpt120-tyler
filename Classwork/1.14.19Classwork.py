# Hailey Tyler
# Lab 5
# 2-14-19

# 1

s1 = "spam"
s2 = "ni!"
# a
print("The Knights who say, " + s2)
# b
print(3 * s1 + 2 * s2)
# c
print(s1[1])
# d
print(s1[1:3])
# e
print(s1[2] + s2[:2])
# f
print(s1 + s2[-1])
# g
print(s1.upper())
# h
print(s2.upper().ljust(4) * 3)

# 2

# a
print(s2[0:2].upper())
# b
print(s2 + s1 + s2)
# c
print(' '.join((s1[0].upper() + s1[1:4], s2[0].upper() + s2[1:3]) * 3))
# d
print(s1)
# e
print([s1[0:2], s1[3]])
# f
print(s1[0:2] + s1[3])

# 3

# a
for ch in "aardvark":
    print(ch)
# b
for w in "Now is the winter of our discontent...".split():
    print(w)
# c
for w in "Mississippi".split("i"):
    print(w, end=" ")

print()

# d
msg = ""
for s in "secret".split("e"):
    msg = msg + s
print(msg)
# e
msg = ""
for ch in "secret":
    msg = msg + chr(ord(ch)+1)
print(msg)

# 4

# a
print("Looks like {1} and {0} for breakfast".format("eggs", "spam"))
# b
print("There is {0} {1} {2} {3}".format(1, "spam", 4, "you"))
# c
print("Hello {0}".format("Susan", "Computewell"))
# d
print("{0:0.2f} {0:0.2f}".format(2.3, 2.3468))
# e
#print("{7.5f} {7.5f}".format(2.3, 2.3468))
# error: index is out of range
# f
print("Time left {0:02}:{1:05.2f}".format(1, 37.374))
# g
#print("{1:3}".format("14"))
# error: index is out of range

# Programming Exercises 4

def acronym():
    print("This is a program that creates acronyms.")
    phrase = input("Type in a phrase.")
    phrase = "".join(i[0] for i in phrase.split())
    print(phrase.upper())
acronym()
