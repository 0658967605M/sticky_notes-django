#input time_taken and saving as a variable
time_taken = int(input("Enter the time taken to finish the triathlon (in minutes): "))
print("Time taken:", time_taken, "minutes") 


#The time taken to finish the triathlon 
if 0 <= time_taken <= 100: #within the qualifying time
    print("Award: Provincial colors")
elif 101 <= time_taken <= 105: # 5 from the qualifying time
    print("Award: Provincial half colors")
elif 106 <= time_taken <= 110: # 10 from the qualifying time
        print("Award: Provincial scroll")
else:
    if 111 <= time_taken:  # more 10 minutes from the qualifying time
        print("Award: No reward") 