#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        subtract = 0
    else:
        subtract = 32
    print(f"{chr(i - subtract)}", end='')
