
import house
import furniture
def run():
    home1 = house.House(120, "五环")
    furn1 = furniture.Furniture('行军床', 2)
    home1.add_furniture(furn1)

    print(home1)
run()



