def analyze_transactions(suspicious, daily):
    if not suspicious:
        return True
    if len(suspicious) > len(daily):
        return False

    i = 0
    for transaction in daily:
        if transaction == suspicious[i]:
            i += 1
            if i == len(suspicious):
                return True
    return False