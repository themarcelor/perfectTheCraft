# -*- coding: utf-8 -*-
"""
We consider two strings to be anagrams of each other if the first string's 
letters can be rearranged to form the second string. In other words, 
both strings must contain the same exact letters in the same exact frequency 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
"""



def number_needed(a, b):
    listA = sorted(list(a))
    listB = sorted(list(b))
    indexB = 0
    indexA = 0
    iguais = 0

    for i in range(max(len(listA),len(listB))):
            
            if listB[indexB] == listA[indexA]:
                indexB+=1
                indexA+=1
                iguais+=1
            else:
                while(listB[indexB] != listA[indexA] and (indexB<len(listB) and indexA<len(listA))):    
                    if ord(listB[indexB]) > ord(listA[indexA]):
                        indexA+=1
                    else:
                        indexB+=1
                    
                    if(indexB == len(listB) or indexA == len(listA) ):
                        return len(listA) + len(listB) - (iguais * 2)
                
            if(indexB == len(listB) or indexA == len(listA) ):
                return len(listA) + len(listB) - (iguais * 2)
                
    return len(listA) + len(listB) - (iguais * 2)

a = "bacdcmdisadmasduasibisncamcaisuias"
b = "dcbacdsaoncainasasokdniudnockm"


if __name__ == '__main__':
       print(number_needed(a,b))
