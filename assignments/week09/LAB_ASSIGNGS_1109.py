def calculate_electricity_cost(units):
    cost = 0
    if units > 200:
        cost = (2.50 * 50) + (3.00 * 50) + (3.50 * 100) + (4.00 * (units - 200)) + 25
    elif units > 100:
        cost = (2.50 * 50) + (3.00 * 50) + (3.50 * (units - 100)) + 25
    elif units > 50:
        cost = (2.50 * 50) + (3.00 * (units - 50)) + 25
    else:
        cost = (2.50 * units) + 25
    return cost
while True:
    print("\nโปรแกรมคำนวนค่าไฟฟ้าจากจำนวนหน่วยไฟฟ้าที่ใช้ในแต่ละเดือน")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        units = float(input("กรอกจำนวนหน่วยไฟฟ้าที่ใช้: "))
        cost = calculate_electricity_cost(units)
        print("\nเอียดค่าไฟฟ้า")
        print("จำนวนหน่วยไฟฟ้า =", units, "หน่วย")
        print("ค่าไฟฟ้ารวมค่าบริการ =", cost, "บาท")
    elif choice == "2":
        print("ออกจากโปรแกรม")
        break
    else:
        raise ValueError("เลือกเมนู1หรือ2เท่านั้น")