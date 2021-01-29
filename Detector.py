print("""


 ___________.__              _______               ___.                        
 \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  ______
   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \/  ___/
   |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/\___ \ 
   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|  /____  >
                 \/     \/          \/            \/    \/     \/           \/ 
                                                         Coded by =>>R00t Devil
""")
print("\033[1;31m1.Jor Sonkha")
print(" ")
print("\033[1;34m2.Bijor Sonkha")
print(" ")
choice = int(input("\033[32m Please select the category 1 or 2 : "))

if choice == 1:
	print(" ")
	from Files import jor
	print(jor)
elif choice ==2:
	print(" ")
	from Files import Bijor
	print(Bijor)
else:
	print("Invalid Input")

