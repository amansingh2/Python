marks = (11 , 12 , 13 , 13 , 13) # tuple doesn't support item assignment , tuples are immutable!
print(marks.count(13))
print(marks.index(12))

'''
[] -> List
() -> tuple , lekin ye parenthesis lagana compulsory ni hota hai!
{} -> sets
'''

#sets : unique elements rakhta hai

scores = {12 , 13 , 14 , 15 , 12 , 13 , 12} # sets ke andar index exist ni karte hai!

for score in scores:
    print(score)




