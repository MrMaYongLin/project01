import furniture
class House():
    def __init__(self, area, address):
        #房屋面积
        self.area = area
        #剩余面积
        self.free_area = area
        #房子地址
        self.address = address
        #家具列表
        self.furniture = []
    def __str__(self):
        return f'房屋位于{self.address},占地面积为{self.area},其中家具有：{self.furniture},之后的剩余面积是{self.free_area}'
    def add_furniture(self, item):
        """容纳家具"""
        if self.free_area >= item.area:
            self.free_area = self.free_area - item.area
            self.furniture.append(item.name)
        else:
            print('家具面积太大，家里无法容纳')

home2 = House(120, '北京')

fu2 = furniture.Furniture('行军锅', 2)
home2.add_furniture(fu2)
print(home2)



