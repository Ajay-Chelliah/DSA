# (1)
"""
*****
*****
*****
*****
*****
"""

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

# (2)
"""
    *
    **
    ***
    ****
    *****
"""
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# (3)
"""
    1
    12
    123
    1234
    12345
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# (4)4
"""
    1
    22
    333
    4444
    5555
"""
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end="")
    print()

# (5)
"""
    *****
    ****
    ***
    **
    *
"""
c = 5
for i in range(c):
    for j in range(c):
        print("*", end="")
    c -= 1
    print()

# (6)
"""
    12345
    1234
    123
    12
    1
"""
c = 5
for i in range(1, c + 1):
    for j in range(1, c + 1):
        print(j, end="")
    c = c - 1
    print()

# (7)
"""
         *         
        ***        
       *****       
      *******      
     ********* 
"""
c = 9
j = 1
for i in range(1, 6):
    mid = c - j // 2
    print(" " * mid + "*" * j + " " * mid)
    j = j + 2

# (8)
"""
*********
 ******* 
  *****  
   ***   
    *  
"""
c = 9
for i in range(5):
    val = c - i * 2
    print(" " * i + "*" * val + " " * i)


# (9)
"""
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
"""


def print_erect_pyramid(rows):
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))


# Example usage:
rows = 5
print("Erect Pyramid:")
print_erect_pyramid(rows)

# (10)

"""
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)

# (11)
"""
    1 
    0 1 
    1 0 1 
    0 1 0 1 
    1 0 1 0 1
"""
for i in range(6):
    for j in range(i):
        print((j % 2) ^ (i % 2), end=" ")
    print()

# (12)
"""
1      1
12    21
123  321
12344321
"""
for i in range(1, 4 + 1):
    space = 4 * 2 - i * 2
    for j in range(1, i + 1):
        print(j, end="")
    print(space * " ", end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# (13)
"""
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
"""
c = 1
for i in range(1, 6):
    for j in range(i):
        print(c, end=" ")
        c += 1
    print()

# (14)
"""
    A 
    A B 
    A B C 
    A B C D 
    A B C D E
"""
c = 65
for i in range(1, 6):
    for j in range(i):
        print(chr(c), end=" ")
        c += 1
    print()
    c = 65

# (15)
"""
    A B C D E 
    A B C D 
    A B C 
    A B 
    A
"""
for i in range(5, 0, -1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

# (16)

"""
    A
    BB
    CCC
    DDDD
    EEEEE
"""
for i in range(5):
    for j in range(i + 1):
        print(chr(65 + i), end="")
    print()

# (17)
"""
   A
  ABA
 ABCBA
ABCDCBA
"""
for i in range(4):
    print(" " * (4 - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end="")
    for j in range(i):
        print(chr(64 + i - j), end="")
    print()

# (18)
"""
    E 
    D E 
    C D E 
    B C D E 
    A B C D E
"""
rows = 5
for i in range(rows):
    for j in range(rows - i, rows + 1):
        print(chr(64 + j), end=" ")
    print()

# (19)
"""
    **********
    ****  ****
    ***    ***
    **      **
    *        *
    *        *
    **      **
    ***    ***
    ****  ****
    **********
"""

for i in range(5, 0, -1):
    print("*" * (i) + " " * (5 - i) * 2 + "*" * (i))
for j in range(1, 6):
    print("*" * (j) + " " * (5 - j) * 2 + "*" * (j))

# (20)
"""
    *        *
    **      **
    ***    ***
    ****  ****
    **********
    **********
    ****  ****
    ***    ***
    **      **
    *        *
"""
for j in range(1, 6):
    print("*" * (j) + " " * (5 - j) * 2 + "*" * (j))
for i in range(5, 0, -1):
    print("*" * (i) + " " * (5 - i) * 2 + "*" * (i))

# (21)

""" 4444444
    4333334
    4322234
    4321234
    4322234
    4333334
    4444444
"""
n = 4
for i in range(n * 2 - 1):
    for j in range(n * 2 - 1):
        top = i
        bottom = (n * 2 - 2) - i
        left = j
        right = n * 2 - 2 - j
        mini = min(min(top, bottom), min(left, right))
        print(n - mini, end="")
    print()
