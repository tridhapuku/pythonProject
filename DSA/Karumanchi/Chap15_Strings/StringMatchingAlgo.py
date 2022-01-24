

def BruteForce(Pattern , StringT):
    StringLen = len(StringT)
    PatternLen = len(Pattern)
    count = 0
    NoOfMatches = 0

    while count < (StringLen - PatternLen + 1):

        if StringT[count] == Pattern[0]:

            if StringT[count:count+PatternLen ] == Pattern[0:PatternLen]:
                print(StringT[count:count+PatternLen ])
                NoOfMatches += 1
                # return True

        count += 1

    return NoOfMatches


#Test for

str1 = 'abcdefaaababcc'
pattern = 'ab'

print(BruteForce(pattern,str1))