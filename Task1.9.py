p = "abcdefghij"
print(p[::-2][:5][::-1][3:])
print("In first step its starting from end and takes 2 steps and form a string so it becomes jhfdb")
print("In 2nd step it chooses the string from 0 index to 5 so it becomes jhfdb")
print("In 3rd step it reverses the string cuz of -1 in the step so it becomes bdfhj")
print("In the last step it chooses to start the string from 3rd index hj")