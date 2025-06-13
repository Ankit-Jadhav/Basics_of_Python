s = int(input("Enter the seconds"))


hours = s%(24*3600)//3600
seconds = s%60 
s = s%3600      #limiting 60 min range
mins = s//60

print("%d:%d:%d"%(hours,mins,seconds))
