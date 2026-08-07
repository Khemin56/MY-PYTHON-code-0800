# รับค่า ชื่อจริง จากผู้ใช้
# เขียน loop เพื่อนับจำนวน " สระที่มีอยู่ในชื่อที่รับมา " นั้นว่ามีจำนวนกี่ตัว
# ตัวอย่างหน้าจอ

# what is you name?: Boonchoo
# Your name hane 4 vowels.
# รับค่า ชื่อจริง จากผู้ใช้
name = "Boonchoo"
vowels = 0
for letter in name:
    print(f" ตัวอักษร: { letter}")
    if letter == 'a' or letter == 'A': 
        vowels = vowels +1

    if letter == 'e' :
        vowels = vowels +1

    if letter in [ 'a' ,'e', 'i', 'o', 'u']:
                vowels = vowels +1
print("Your name have ,vowels ,vowels")
print(f"Your name have {vowels} vowels")
