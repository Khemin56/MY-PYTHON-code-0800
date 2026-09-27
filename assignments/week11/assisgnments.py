def deposit(money):
    balance = 1000.0
    try:
        amount = float(money)
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
    except ValueError as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")
    else:
        balance += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")

print("ยอดเงินเริ่มต้น: 1000 บาท")
user_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
deposit(user_input)