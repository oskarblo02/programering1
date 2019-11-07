print("this program calculates  the kinetic energy of a moving object")
m_string = input("enter the objects mass in kgs: ")
m = float(m_string)
v_string = input("enter the objects speed in m/s: ")
v = float(v_string)

e = 0.5 * m * v * v
print("this object has " + str(e) + "joules of energy.")
