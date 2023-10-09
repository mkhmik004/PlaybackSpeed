
#MMM MKHABELE
#28/06/2023
def playback(n):
    n=n.split() #creates list of sting from input
    for i in range(len(n)): #iterate through and print all elements in the key ending with ***
        print(n[i],sep='',end="")
        if i<(len(n)-1):#terminate print(***) for last ***
            print("...",end="")
def main():
    string=input("Enter String/script to palyback:\n")
    playback(string) #calling playback funtion 
main()
