from numpy import test


class Program(object):
    opp_map = {
        "inp": lambda x,y: y,
        "add": lambda x,y: x+y,
        "mul": lambda x,y: x*y,
        "div": lambda x,y: x//y,
        "mod": lambda x,y: x%y,
        "eql": lambda x,y: int(x==y)
    }
    def __init__(self,w,x =0,y =0,z = 0):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def run_line(self, line):
        line_split = line.split()
        opp, a, b = line_split
        if hasattr(self, b):
            b = getattr(self,b)
        else:
            b = int(b)
        setattr(self,a, self.opp_map[opp](getattr(self, a),b))
    def run_lines(self,lines):
        for line in lines:
            self.run_line(line)
    def __repr__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}, w: {self.w}"




ints = open('D24input.txt','r').read().splitlines()
for zz in range(-1000,1000):
    for digits in range(1,10):

        test_program = Program(digits, z=zz )
        test_program.run_lines(ints)
        if test_program.z <10 and test_program.z > 0:
            print(digits, zz)
            print(test_program)
        