def substrEnterances(string, substring):
    ans = 0
    while string.find(substring) != -1:
        ans += 1
        string = string[string.find(substring) + 1::]
        # print(string)

    return ans


s = input()
substr = input()
print(substrEnterances(s, substr))
