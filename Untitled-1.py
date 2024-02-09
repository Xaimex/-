class Chair:

    def __init__(self, legs, material, company):
        self.legs = legs     
        self.company = company
        self.material = material


    def display_info(self):
        print(f"legs: {self.legs}  material: {self.material} company: {self.company}")
    def __str__(self):
        return self.legs
    def __repr__(self):
        return f'Chair(\'{self.legs}\', {self.material}, {self.company})'


tab = Chair(4,"steel","dxracer")
tron = Chair(5,"wood","dxseat")

print(repr(tab))