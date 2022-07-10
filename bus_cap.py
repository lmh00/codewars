def enough(cap, on, wait):
    return wait - cap + on if wait > cap - on else 0

enough(20, 5, 5)
