def ballassignunassignFinder(holes_list,
                             balls_list):
    # Stores the assigned and unassigned of balls
    assigned_ball = []
    unassigned_ball = []
    assigned_hole = []

    # Iterate over all possible holes
    # for every ball released
    for i in balls_list:
        for j in holes_list:

            # Place ball in hole if it fits
            #print(i)
            #print(j)
            if (j >= i) and j not in assigned_hole:
                assigned_ball.append(i)
                assigned_hole.append(j)
                break

            # If ball has reached at end B
            if j == len(holes_list):
                unassigned_ball.append(i)
                break
            #print(assigned_ball)
            #print(assigned_hole)
            #print(unassigned_ball)

    return (assigned_ball, unassigned_ball)


# Driver Code
if __name__ == "__main__":

    holes_list = [21, 3, 12]

    balls_list = [25, 15, 5, 8]

    holes_list.sort(reverse=True)
    balls_list.sort(reverse=True)

    # Function Call
    assigned_ball, unassigned_ball = ballassignunassignFinder(holes_list,
                                                              balls_list)

    print("Assigned Ball:", *assigned_ball)
    print("Unassigned ball:", *unassigned_ball)
    print("Ball Hole Pairs")
    for x, y in zip(assigned_ball, holes_list):
        print(x, y)