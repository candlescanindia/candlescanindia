def is_inverted_hammer(row):
    body = abs(row['Close'] - row['Open'])
    lower = min(row['Open'], row['Close']) - row['Low']
    upper = row['High'] - max(row['Open'], row['Close'])
    return upper > 2 * body and lower < body

def is_shooting_star(row):
    body = abs(row['Close'] - row['Open'])
    upper = row['High'] - max(row['Open'], row['Close'])
    lower = min(row['Open'], row['Close']) - row['Low']
    return upper > 2 * body and lower < body

def is_hanging_man(row):
    return is_hammer(row)

def is_spinning_top(row):
    body = abs(row['Close'] - row['Open'])
    total_range = row['High'] - row['Low']
    return body < 0.3 * total_range

def is_marubozu(row):
    return abs(row['Close'] - row['Open']) > 0.95 * (row['High'] - row['Low'])
