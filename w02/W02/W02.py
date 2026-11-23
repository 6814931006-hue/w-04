from Student import Student
from Building import Building
from Room import Room
from Subject import Subject
from Lecturer import Lecturer
from Course import Course
from Enrollment import Enrollment

# 1. สร้างข้อมูลนักศึกษา
s01 = Student("6814931006", "นายเตย์ศิษย์ โศภิษฐ์สิทธิกุล")

# 2. สร้างห้องและตึก 4 ตามตารางเรียน
b4 = Building("4")
r434 = Room("434", b4)
r436 = Room("436", b4)
r438 = Room("438", b4)
b4.addRoom(r434)
b4.addRoom(r436)
b4.addRoom(r438)

# สร้างห้องและตึก 35 ตามตารางเรียน
b35 = Building("35")
r35408 = Room("35408", b35)
b35.addRoom(r35408)

# 3. สร้างรายวิชาทั้ง 6 วิชาตามตารางเรียน
sub1 = Subject("9043042-55", "มาตรฐานทางภูมิสารสนเทศ", 3)
sub2 = Subject("9042051-55", "การเขียนโปรแกรมเชิงวัตถุสำหรับภูมิสารสนเทศ", 3)
sub3 = Subject("9043041-59", "การวิเคราะห์และการจำลองเชิงพื้นที่", 3)
sub4 = Subject("0265011-65", "การเข้าใจดิจิทัลเพื่อความเป็นนวัตกร", 3)
sub5 = Subject("9042052-59", "การเขียนโปรแกรมเว็บขั้นสูง", 3)
sub6 = Subject("9042041-55", "การจัดการฐานข้อมูลในระบบสารสนเทศภูมิศาสตร์", 3)

# 4. สร้างอาจารย์ผู้สอนตามตารางเรียน (4 ท่าน)
lec1 = Lecturer("อาจารย์ภูมิพัฒน์ อุ่นบ้าน")
lec2 = Lecturer("อาจารย์นิทัศน์ นิลฉวี")
lec3 = Lecturer("ผู้ช่วยศาสตราจารย์วีระ ศรีมาลา")
lec4 = Lecturer("ผู้ช่วยศาสตราจารย์ ดร. ภูวดล บัวบางพลู")

# 5. สร้างคลาสเรียน (Course) เชื่อมวิชา อาจารย์ และห้องเรียน
c1 = Course(1, sub1, lec1, r438)
c2 = Course(1, sub2, lec2, r436)
c3 = Course(1, sub3, lec3, r434)
c4 = Course(1, sub4, lec4, r35408)
c5 = Course(1, sub5, lec2, r434)
c6 = Course(1, sub6, lec3, r438)

# 6. สร้างการลงทะเบียนเรียน (Enrollment)
enroll = Enrollment(1, 2568, s01)
enroll.addCourse(c1)
enroll.addCourse(c2)
enroll.addCourse(c3)
enroll.addCourse(c4)
enroll.addCourse(c5)
enroll.addCourse(c6)

# --- สั่งปริ้นตึกและห้องเรียน (เหมือนต้นฉบับ) ---
print(b4)
b4.listRooms()

print(b35)
b35.listRooms()
print()

# --- สั่งปริ้นข้อมูลการลงทะเบียนทั้งหมด ---
enroll.showEnrollment()