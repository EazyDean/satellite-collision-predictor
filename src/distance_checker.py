from scipy.spatial.distance import euclidean

def check_collisions(positions_list, threshold_km=1.0):
    n = len(positions_list)
    risks = []
    for i in range(n):
        for j in range(i + 1, n):
            distances = [euclidean(p1, p2) for p1, p2 in zip(positions_list[i], positions_list[j])]
            close = [d for d in distances if d < threshold_km]
            if close:
                risks.append((i, j, min(close)))
    return risks