
#ITM (CWN Series)
#Module Time
#time.time()
#time.sleep()
#1η Ιανουαρίου 1970,12:00 π.μ (Unix Epoch)

import time #εισαγωγή του αρθρώματος time
start = time.time() #αρχή μέτρησης για την εκτέλεση του προγράμματος
print("Hello Nick")
time.sleep(2) #παύση εκτέλεσης προγράμματος για 2 δευτερόλεπτα
for i in range(1,50):
    print(i)
time.sleep(5) #παύση εκτέλεσης προγράμματος για 5 δευτερόλεπτα
name = input("Give me your name: ")
print("Thanks,",name,"!")
end = time.time() #τέλος μέτρησης για την εκτέλεση του προγράμματος
full_time = end -start #τελικός χρόνος εκτέλεσης του προγράμματος
print(full_time)
