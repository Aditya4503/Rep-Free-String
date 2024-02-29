def repfree(s):
    repeatation = True
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if i!=j and s[i]==s[j]:
                repeatation = False
                break
    return repeatation

repfree("alpha_maverick")

#Code by : alpha_maverick
            
