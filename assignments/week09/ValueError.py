""" โจทย์ 1: เครื่องคำนวณอย่างปลอดภัย
เขียนโปรแกรมรับตัวเลข 2 จำนวนและตัวดำเนินการ 1 ตัว ได้แก่ +, -, *, / 
แล้วแสดงผลลัพธ์ 
โปรแกรมต้องจัดการกรณีต่อไปนี้
*ผู้ใช้กรอกข้อมูลที่ไม่ใช่ตัวเลข # ValueError
*ผู้ใช้เลือกตัวดำเนินการอื่นนอกเหนือจาก +, -, *, / # raise ValueError
*ผู้ใช้พยายามหารด้วยศูนย์ # ZeroDivisionError
*โปรแกรมต้องแสดง "จบการทำงาน" เสมอด้วย finally """
try:
    number1 = float(input("ตัวเลขที่ 1: "))
    number2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")
    if operator not in ['+', '-', '*', '/']:
        raise ValueError("เครื่องหมายไม่ถูกต้อง")
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        result = number1 / number2
    print(f"ผลลัพธ์: {result}")
except ValueError:
    print("ข้อมูลไม่ถูกต้อง")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
finally:
    print("จบการทำงาน")