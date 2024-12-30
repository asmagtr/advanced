string=input("enter a word : ")
frame_r=(28-len(string))//2
frame_l=frame_r
if(len(string)%2==1):
    frame_r=frame_r+1


print("*"*30)
print("*"+" "*frame_l+string+" "*frame_r+"*")
print("*"*30)