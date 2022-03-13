# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

first_height = int(student_scores[0])
highest = 0

for score in student_scores:

    if score > highest:
        highest = score
    else:
        0

if first_height > highest:
    print(f"The highest score in the class is: {first_height}")
else:
    print(f"The highest score in the class is: {highest}")


