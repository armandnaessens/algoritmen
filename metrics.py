from numpy import zeros

def levenshtein_distance_recursive(string_a, string_b, i = -1, j = -1):
    if i == - 1 and j == - 1:
        i = len(string_a)
        j = len(string_b)
    if min(i, j) == 0:
        return max(i, j)
    I = string_a[i - 1] != string_b[j - 1]
    return min(levenshtein_distance_recursive(string_a, string_b, i - 1, j) + 1, levenshtein_distance_recursive(string_a, string_b,i, j - 1) + 1, levenshtein_distance_recursive(string_a, string_b, i - 1, j - 1) + I)

def levenshtein_distance_DP(str1,str2):
    if (len(str1) > len(str2)):
        temp = str1
        str1 = str2
        str2 = temp
    i = len(str1)
    j = len(str2)
    C = [[] for l in range(j)]
    k = 1
    for el in range(j):
        C[el] = zeros(k)
        if k < i:
            k += 1
    "C[0][0] = str1[0] != str2[0]"
    for l in range(j):
        for k in range(l, i):
            if l == 0 and k == 0:
                C[k][l] = 0
            elif l == 0:
                C[k][l] = C[k - 1][l] + 1
            elif k == l:
                C[k][l] = min(C[k][l - 1] + 1, C[k - 1][l - 1] + (str1[k] != str2[l]))
            else:
                C[k][l] = min(C[k][l - 1] + 1, C[k - 1][l - 1] + (str1[k] != str2[l]), C[k - 1][l] + 1)
    if j > i:
        for l in range(i):
            for k in range(i, j):
                if l == 0:
                   C[k][l] = C[k - 1][l] + 1
                else:
                    C[k][l] = min(C[k][l - 1] + 1, C[k - 1][l - 1] + (str1[-1] != str2[l]), C[k - 1][l] + 1)
    return int(C[j - 1][i - 1])