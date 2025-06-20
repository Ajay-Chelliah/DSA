def merge(intervals):
    # Step 1: Sort intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged = []

    for interval in intervals:
        # if merged is empty or no overlap
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # there's overlap, merge intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged
