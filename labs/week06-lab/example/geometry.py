# Example 3: Mathematical function
def calculate_triangle_area(height, base):
    """Calculates and displays rectangle area"""
    area = height * width
    print(f"Triangle with height {height} and width {width}")
    print(f"Area = {height} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_triangle_area(5, 3)
calculate_triangle_area(10, 7)

def calculate_circle_area(radius):
    pass

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