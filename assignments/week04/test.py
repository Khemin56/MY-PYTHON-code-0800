# รับค่า ชื่อจริง จากผู้ใช้
# เขียน loop เพื่อนับจำนวน " สระที่มีอยู่ในชื่อที่รับมา " นั้นว่ามีจำนวนกี่ตัว
# ตัวอย่างหน้าจอ

# what is you name?: Boonchoo
# Your name hane 4 vowels.
# รับค่า ชื่อจริง จากผู้ใช้
# รับค่าชื่อจริงจากผู้ใช้
name = input("What is your name?: ")
vowels = 0

for letter in name:
    print(f"ตัวอักษร: {letter}")
    if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowels = vowels + 1

print(f"Your name has {vowels} vowels.")