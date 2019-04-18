'''Input permutation: given s='abc' the function should return ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']'''
#Doubt
def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        for i, letter in enumerate(s):
            # print("i",i)
            # print("letter",letter)
            for per in permute(s[:i] + s[i+1: ]):
                # print(s[:i] + s[i+1: ])
                out += [letter + per]
                # print('out', out)

    return out
print(permute('abc'))