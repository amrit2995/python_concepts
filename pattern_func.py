def pattern(n):

    out = []

    for i in range(n):
        row = []
        for j in range(i+1):
            # if not out:
            #     row.append(1)
            if j-1 < 0:
                row.append(1)
            elif j >= len(out[-1]):
                row.append(1)
            else:
                row.append(out[-1][j]+out[-1][j-1])
        out.append(row)
    return out

print(pattern(4))
# print()