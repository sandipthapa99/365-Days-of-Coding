# Break                     # --------
for num in range(4):        # Result:
    if num == 2:            # --------
        break               # 0
    print(num)              # 1
                            # -------

# Continue                  # --------
for num in range(4):        # Result:
    if num == 2:            # --------
        continue            # 0
    print(num)              # 1
                            # 3
                            # --------