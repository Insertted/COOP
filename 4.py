tp = input().strip();

if tp == "RECT":
    def get_sq(length, width):
        return length * width;
else:
    def get_sq(sq_side):
        return sq_side * sq_side;

print(get_sq);