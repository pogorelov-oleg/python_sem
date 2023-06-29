string = {"1": "222anton456", "2": "a1n1t1o1n1", "3": "0000a0000n00t00000o000000n", "4": "gylfole", "5": "richard", "6": "ant0n"}              

def Check_Virus(string, virus):
    for i in virus:
            if i not in string:
                return("Ok")
            else:
                string = string[string.index(i):]
    return("Virus")    
          

for i in string: 
    print(f'{i} - {Check_Virus(string[i], "anton")}')



