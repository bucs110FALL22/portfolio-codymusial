
def star_pyramid():
  levels = int(input("Enter the desired pyramid height: "))
  for i in range (1, levels + 1):
    print("*" * i)

def rstar_pyramid():
  levels = int(input("Enter the desired pyramid height: "))
  for i in range(levels, 0, -1):
    print("*" * i)

star_pyramid()
rstar_pyramid()