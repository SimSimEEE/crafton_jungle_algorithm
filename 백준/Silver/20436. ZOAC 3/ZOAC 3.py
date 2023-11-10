SL, SR = input().split()
word = input()
keyboard = {
  'q':('l',0,0),'w':('l',0,1),'e':('l',0,2),'r':('l',0,3),'t':('l',0,4),'y':('r',0,5),'u':('r',0,6),'i':('r',0,7),'o':('r',0,8),'p':('r',0,9),
  'a':('l',1,0),'s':('l',1,1),'d':('l',1,2),'f':('l',1,3),'g':('l',1,4),'h':('r',1,5),'j':('r',1,6),'k':('r',1,7),'l':('r',1,8),
  'z':('l',2,0),'x':('l',2,1),'c':('l',2,2),'v':('l',2,3),'b':('r',2,4),'n':('r',2,5),'m':('r',2,6),
}
result = 0
for alpha in word:
    hand, row, col = keyboard[alpha]
    result += 1
    if hand == 'l':
        result += abs(row - keyboard[SL][1]) + abs(col - keyboard[SL][2])
        SL = alpha
    else: 
        result += abs(row - keyboard[SR][1]) + abs(col - keyboard[SR][2])
        SR = alpha
print(result)