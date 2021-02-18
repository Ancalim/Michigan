def MaxValue(z):
    for best_value in MaxValue(z):
        if best_value > MaxValue(z):
            return best_value


z=MaxValue([1,2])
