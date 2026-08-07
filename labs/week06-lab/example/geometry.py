# Example 3: Mathematical function
import math
def calculate_triangle_area(height, base):
    """Calculates and displays triangle area."""
    if height < 0 or base < 0:
        print("Error: Height and base cannot be negative.")
        return None
    area = 0.5 * height * base
    print(f"Triangle with height {height} and base {base}")
    print(f"Area = 0.5 × {height} × {base} = {area:.2f}")
    print()
    return area
def calculate_circle_area(radius):
    """Calculates and displays circle area."""
    if radius < 0:
        print("Error: Radius cannot be negative.")
        return None
    area = math.pi * (radius**2)
    print(f"Circle with radius {radius}")
    print(f"Area = π × {radius}² = {area:.2f}")
    print()
    return area
# เขียน function ชื่อ calculate_sphere(radius):
# คำนวณฟา ปริมาตร ของทรงกลม volum = 4.0 /3* ยร * radius ** 3
# จากนั้นแสดงผลลัพธ์ที่เหมาะสมออกทางหน้าจอ
# ไม่ลืมที่จะเขียนโปรแกรมในส่วนของการทดสอบการใช้งาน
import math
def calculate_sphere(radius):
    """Calculates and displays the volume of a sphere."""
    if radius < 0:
        print("Error: Radius cannot be negative.")
        return None
    volume = (4.0 / 3.0) * math.pi * (radius**3)
    print(
        f"Sphere Radius: {radius} units -> Volume = {volume:.2f} cubic units"
    )
    return volume
if __name__ == "__main__":
    print("--- Starting Function Tests ---")
    calculate_sphere(5)
    calculate_sphere(2.5)
    calculate_sphere(0)
    calculate_sphere(-3)