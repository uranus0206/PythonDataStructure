Score = [87, 66, 90, 65, 70]

Total_Score = 0

for count in range(5):
    print("Score of %d's student is %d" %(count+1, Score[count]))
    Total_Score += Score[count]
    
print("--------------------------")
print("Total score of five students: %d" %Total_Score)
    