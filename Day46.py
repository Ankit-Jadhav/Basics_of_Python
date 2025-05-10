#os modules
#create file in easy way
import os
# os.mkdir("data")

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")


#rename folders
for i in range(0,100):
    os.rename(f"data/Day{i+1}",f"data/tutorial{i+1}")



# we can search folder also.
# there are multiple methods in os module. refer document and check it, use it


    
