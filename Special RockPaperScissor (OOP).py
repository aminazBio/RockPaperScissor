class Tool:
    def __init__(self,Power,Type):
        self.Power=Power
        self.Type=Type
    def SetPower(self,Power):
        self.power=Power

class Rock(Tool):
    def __init__(self,Power):
        self.tool=Tool(self.SetPower(Power),'r')
    def Fight(self,f):
        if self.power > f:
            return 1
        elif self.power < f: 
            return -1
        else: 
            return 0       

class Paper(Tool):
    def __init__(self,Power):
        self.tool=Tool(self.SetPower(Power),'p')
    def Fight(self,f):
        if self.power > f:
            return 1
        elif self.power < f: 
            return -1
        else: 
            return 0

class Scissors(Tool):
    def __init__(self,Power):
        self.tool=Tool(self.SetPower(Power),'s')
    def Fight(self,f):
        if self.power > f:
            return 1
        elif self.power < f: 
            return -1
        else: 
            return 0

n=input().split()
r=int(n[0])
p=int(n[1])
s=int(n[2])


rock=Rock(r)
paper=Paper(p)
scissors=Scissors(s)



print('\    R    P    S')


print('R',end='    ')

print('E',end='    ')

r2=rock.Fight(p*2)
if r2 == 1:
    print('W',end='    ')
elif r2 == -1: 
    print('L',end='    ') 
else:
    print('E',end='    ') 

r3=rock.Fight(s/2)
if r3 == 1:
    print('W')
elif r3 == -1: 
    print('L') 
else:
    print('E')


print('P',end='    ')

p1=paper.Fight(r/2)
if p1 == 1:
    print('W',end='    ')
elif p1 == -1: 
    print('L',end='    ') 
else:
    print('E',end='    ') 

print('E',end='    ')

p3=paper.Fight(s*2)
if p3 == 1:
    print('W')
elif p3 == -1: 
    print('L') 
else:
    print('E')


print('S',end='    ')

s1=scissors.Fight(r*2)
if s1 == 1:
    print('W',end='    ')
elif s1 == -1: 
    print('L',end='    ') 
else:
    print('E',end='    ')

s2=scissors.Fight(p/2)
if s2 == 1:
    print('W',end='    ')
elif s2 == -1: 
    print('L',end='    ') 
else:
    print('E',end='    ')

print('E')

