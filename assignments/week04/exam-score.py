scores = []
print("Enter score of student 1 to 5:")
for i in range(1, 6):
    score = float(input(f"Enter score of student {i}: "))
    scores.append(score)
print()
for i in range(5):
    student_num = i + 1
    score = scores[i]
    
    display_score = int(score) if score.is_integer() else score
    if score >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"   
    print(f"Student {student_num}: {display_score} -> {result}")