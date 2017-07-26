
import csv

def inner(cell, spreadsheet):
    try:
        parts = cell.split()
        if len(parts) == 0:
            return 0.0

        stack = []
        for part in parts:
            if part[0].isalpha():
                col = ord(part[0]) - ord('a')
                row = int(part[1:]) - 1
                cell = spreadsheet[row][col]
                value = solve(cell, spreadsheet)
                if value == "#ERR":
                    return "#ERR"

                stack.append(value)
            elif part[0].isdigit() or part[0] == '.':
                value = float(part)

                stack.append(value)
            elif part in ('+', '-', '*', '/'):
                a = stack.pop()
                b = stack.pop()
                if part == '+':
                    stack.append(a + b)
                elif part == '-':
                    stack.append(b - a)
                elif part == '*':
                    stack.append(a * b)
                elif part == '/':
                    stack.append(b / a)
            else:
                return "#ERR"

        if len(stack) != 1:
            return "#ERR"

        return stack.pop()
    except:
        return "#ERR"

visited = {}
def solve(cell, spreadsheet):
    if cell in visited:
        computed = visited[cell]
        if computed is None:
            # cycle detected
            return "#ERR"

        return computed

    visited[cell] = None
    value = inner(cell, spreadsheet)
    visited[cell] = value
    return value

if __name__ == "__main__":
    rows = []

    with open('input.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)

    output_rows = []
    for row in rows:

        output_row = []
        for cell in row:
            output_row.append(solve(cell, rows))

        output_rows.append(output_row)

    with open('solution.csv', 'w') as f:
        writer = csv.writer(f)
        for row in output_rows:
            writer.writerow(row)
