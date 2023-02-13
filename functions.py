def get_summ(one, two, delimiter='&'):
    return delimiter.join([str(one), str(two)])


summ = get_summ('Learn', 'python')
print(summ.upper())
