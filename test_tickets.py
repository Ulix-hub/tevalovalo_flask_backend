
from ticket_generator_module import generate_full_strip

def validate_ticket(ticket):
    all_cols = set()
    total_numbers = 0
    for row in ticket:
        count = sum(1 for n in row if n is not None)
        if count != 5:
            return False, "Row does not have exactly 5 numbers"
        total_numbers += count
        for i, val in enumerate(row):
            if val is not None:
                all_cols.add(i)
    if total_numbers != 15:
        return False, "Ticket does not have 15 numbers"
    if len(all_cols) != 9:
        return False, "Ticket does not use all 9 columns"
    return True, "Valid"

tickets = generate_full_strip()
for i, ticket in enumerate(tickets):
    valid, message = validate_ticket(ticket)
    print(f"Ticket {i+1}: {'✅' if valid else '❌'} - {message}")
