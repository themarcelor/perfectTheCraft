import re
import timeit

str = 'Hi there!'
ls = 'aeiou'

def vowels(str):
    count = 0

    for l in re.sub(r'[^a-zA-Z]','',str.lower()):
        if l in ls:
            count += 1

    return count

def vowels_easy_sub(str):
    # print re.sub(r'[^aeiou]', '', str.lower()) #iee
    return len(re.sub(r'[^%s]' % (ls), '', str.lower()))

#winner
def vowels_easy_findall(str):
    # print re.findall('[aeiou]', str.lower()) #['i','e','e']
    return len( re.findall('[aeiou]', str.lower()) )


print vowels(str)
print vowels_easy_sub(str)
print vowels_easy_findall(str)

if __name__ == '__main__':
    print timeit.timeit("vowels(str)", "from __main__ import vowels, str", number=100)
    print timeit.timeit("vowels_easy_sub(str)", "from __main__ import vowels_easy_sub, str", number=100)
    print timeit.timeit("vowels_easy_findall(str)", "from __main__ import vowels_easy_findall, str", number=100)
