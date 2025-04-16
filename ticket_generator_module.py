import random

COLUMN_RANGES = {
    0: list(range(1, 10)),
    1: list(range(10, 20)),
    2: list(range(20, 30)),
    3: list(range(30, 40)),
    4: list(range(40, 50)),
    5: list(range(50, 60)),
    6: list(range(60, 70)),
    7: list(range(70, 80)),
    8: list(range(80, 91)),
}

def generate_full_strip():
    while True:
        try:
            col_distribution = {0: 9, 8: 11}
            for c in range(1, 8):
                col_distribution[c] = 10

            # Prepare column numbers
            column_numbers = {
                c: random.sample(COLUMN_RANGES[c], col_distribution[c])
                for c in range(9)
            }

            strip = []
            used_numbers = set()

            for _ in range(6):
                ticket = [[None for _ in range(9)] for _ in range(3)]
                row_counts = [0, 0, 0]
                col_counts = [0] * 9
                filled = 0
                attempts = 0

                while filled < 15 and attempts < 100:
                    r = random.randint(0, 2)
                    c = random.randint(0, 8)
                    if (
                        ticket[r][c] is None
                        and row_counts[r] < 5
                        and col_counts[c] < 3
                        and column_numbers[c]
                    ):
                        n = column_numbers[c].pop()
                        if n not in used_numbers:
                            ticket[r][c] = n
                            used_numbers.add(n)
                            row_counts[r] += 1
                            col_counts[c] += 1
                            filled += 1
                    attempts += 1

                if filled < 15 or any(row.count(None) != 4 for row in ticket):
                    raise Exception("Ticket fill failed. Retrying...")

                strip.append(ticket)

            # ✅ Enforce column-wise ascending order within each ticket
            for ticket in strip:
                for col in range(9):
                    col_nums = [ticket[row][col] for row in range(3) if ticket[row][col] is not None]
                    col_nums.sort()
                    i = 0
                    for row in range(3):
                        if ticket[row][col] is not None:
                            ticket[row][col] = col_nums[i]
                            i += 1

            return strip

        except:
            continue
