import matplotlib.pyplot as plt
import itertools

def plot_flight_paths(flight_paths):
    for flight, path in flight_paths.items():
        x_coords = [point[0] for point in path]
        y_coords = [point[1] for point in path]
        plt.plot(x_coords, y_coords, marker='o', label=flight)
    
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Flight Paths')
    plt.legend()
    plt.show()

def do_intersect(line1, line2):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0: return 0  # collinear
        return 1 if val > 0 else 2  # clockwise or counterclockwise

    def on_segment(p, q, r):
        if min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1]):
            return True
        return False

    p1, q1 = line1
    p2, q2 = line2

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and on_segment(p1, p2, q1): return True
    if o2 == 0 and on_segment(p1, q2, q1): return True
    if o3 == 0 and on_segment(p2, p1, q2): return True
    if o4 == 0 and on_segment(p2, q1, q2): return True

    return False

def adjust_paths(flights):
    all_lines = []
    flight_paths = list(flights.values())
    
    for path in flight_paths:
        for i in range(len(path) - 1):
            all_lines.append(((path[i][0], path[i][1]), (path[i + 1][0], path[i + 1][1])))

    adjusted_paths = {name: path.copy() for name, path in flights.items()}
    
    for (line1, line2) in itertools.combinations(all_lines, 2):
        if do_intersect(line1, line2):
            # Shift endpoints of the first line
            for path in adjusted_paths.values():
                for i in range(len(path) - 1):
                    if (path[i], path[i+1]) == line1:
                        path[i+1] = (path[i+1][0] + 1, path[i+1][1] + 1)
                    if (path[i], path[i+1]) == line2:
                        path[i+1] = (path[i+1][0] - 1, path[i+1][1] - 1)

    # Remove potential duplicates due to adjustments
    for path in adjusted_paths.values():
        path[:] = list(dict.fromkeys(path))

    return adjusted_paths

def main():
    flights = {}
    num_flights = int(input("Enter the number of flights: "))
    
    for i in range(num_flights):
        flight_name = f'Flight {i + 1}'
        flights[flight_name] = []
        print(f"Enter coordinates for {flight_name} (enter -1 -1 to stop):")
        while True:
            x, y = map(int, input().split())
            if x == -1 and y == -1:
                break
            flights[flight_name].append((x, y))
    
    adjusted_flights = adjust_paths(flights)
    plot_flight_paths(adjusted_flights)

if __name__ == "__main__":
    main()
