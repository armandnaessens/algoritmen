def levenshtein_recursive(string_a, string_b,i = -1, j = -1):
    if i == - 1 and j == - 1:
        i = len(string_a)
        j = len(string_b)
    if min(i, j) == 0:
        return max(i, j)
    I = string_a[i - 1] != string_b[j - 1]
    return min(levenshtein_recursive(string_a, string_b, i - 1, j) + 1, levenshtein_recursive(string_a, string_b,i, j - 1) + 1, levenshtein_recursive(string_a, string_b, i - 1, j - 1) + I)