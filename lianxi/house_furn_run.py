
import house
import furniture

if __name__ == '__main__':
    home1 = house.House(120, "五环")
    furn1 = furniture.Furniture('行军床', 2)
    home1.add_furniture(furn1)
    print(home1)

