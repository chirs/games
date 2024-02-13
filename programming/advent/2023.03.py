import advent

'''
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''


def create_map(s):

    lines = s.split('\n')

    coord_dict = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            coord_dict[(x, y)] = char

    x_dim = max([x for (x, y) in coord_dict.keys()]) + 1
    y_dim = max([y for (x, y) in coord_dict.keys()]) + 1

    m = Map(coord_dict, (x_dim, y_dim))

    return m



class Map(object):

    def __init__(self, coord_dict, dimensions):
        self.coord_dict = coord_dict
        self.dimensions = dimensions


    def get_value_string(self, coords):
        return ''.join([self.coord_dict[c] for c in coords])


    def find_gear_coords(self):
        gears = []
        for coord, value in self.coord_dict.items():
            if value == '*':
                gears.append(coord)

        return gears
    
    
    def find_number_coords(self):
        numerals = set('0123456789')
        number_coords = []
        for coord, value in self.coord_dict.items():
            if value in numerals:
                number_coords.append(coord)

        def walk_forward(coord):
            cx = [coord]
            x, y = coord

            for i in range(1, self.dimensions[0]):
                c = (x+i, y)
                if self.coord_dict.get(c, None) in numerals:
                    cx.append(c)
                else:
                    return cx

        number_coords_set = set(number_coords)                
        number_coords_list = []

        for x, y in number_coords:
            if (x-1, y) in number_coords_set:
                pass
            else:
                # first item in the numeral
                number_coords = walk_forward((x, y))
                number_coords_list.append(number_coords)

        return number_coords_list
                
                

    def is_valid(self, coord):
        x, y = coord
        if x < 0 or x > self.dimensions[0] - 1:
            return False
        if y < 0 or y > self.dimensions[1] - 1:
            return False
        else:
            return True
        

    def adjacent_coords(self, coord):
        # includes diagonals
        x, y = coord
        cx = [
            (x-1, y),
            (x, y-1),                
            (x, y+1),
            (x+1, y),
            # (x, y),                
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y-1),
            (x+1, y+1),
        ]
        
        return [c for c in cx if self.is_valid(c)]

    
class MapNumber(object):

    def __init__(self, map, coords):
        self.map = map
        self.coords = coords

        self.value = int(self.map.get_value_string(coords))


    def is_part_number(self):
        adjacent_coords = set()
        for coord in self.coords:
            for ac in self.map.adjacent_coords(coord):
                adjacent_coords.add(ac)

        for coord in self.coords:
            adjacent_coords.discard(coord)

        adjacent_values = self.map.get_value_string(adjacent_coords)

        if set(adjacent_values) == set('.'):
            return False
        else:
            return True


class Gear(object):

    def __init__(self, map, coord):
        self.map = map
        self.coord = coord

    def ratio(self):
        numbers = self.get_numbers()
        if len(numbers) != 2:
            return 0
        else:
            n1, n2 = numbers
            import pdb; pdb.set_trace()
            return n1.value * n2.value

        
    def get_numbers(self):

        adjacent_coords = set(self.map.adjacent_coords(self.coord))

        def is_adjacent_number(number_coords):
            for number_coord in number_coords:
                if number_coord in adjacent_coords:
                    return True
            return False

        all_number_coords = self.map.find_number_coords()
        adjacent_number_coords = [e for e in all_number_coords if is_adjacent_number(e)]

        return adjacent_number_coords
            
        

def part1():
    s = open('2023.03.input').read()
    engine_schematic = create_map(s)
    numbers = engine_schematic.find_number_coords()

    schematic_numbers = [MapNumber(engine_schematic, n) for n in numbers]

    invalid = schematic_numbers[2]

    valid_numbers = [e.value for e in schematic_numbers if e.is_part_number()]

    return sum(valid_numbers)


def part2():

    s = open('2023.03.input').read()
    engine_schematic = create_map(s)
    numbers = engine_schematic.find_number_coords()
    schematic_numbers = [MapNumber(engine_schematic, n) for n in numbers]

    gear_coords = engine_schematic.find_gear_coords()
    gears = [Gear(engine_schematic, coord) for coord in gear_coords]
    
    return sum([gear.ratio() for gear in gears])
    
    
    

if __name__ == "__main__":
    a = part1()
    print(a)
    b = part2()
    print(b)
    
    
