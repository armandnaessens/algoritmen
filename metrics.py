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
    if len(str1) < len(str2):
        temp = str1
        str1 = str2
        str2 = temp
    k = len(str1)
    l = len(str2)
    C = [zeros(l + 1) for i in range(k + 1)]
    for i in range(k):
        C[i][0] = i
    for i in range(l):
        C[0][i] = i
    for i in range(1, l + 1):
        for j in range(1, k + 1):
            C[i][j] = min(C[i - 1][j] + 1, C[i][j - 1] + 1, C[i - 1][j - 1] + (str1[i - 1] != str2[j - 1]))
    return C[k][l]