def tower_of_hanoi(n, source, destination, auxiliary):
    """
    This function implements the Tower of Hanoi algorithm recursively.

    n - the number of disks to move
    source - the rod from which to move the disks
    destination - the rod to which to move the disks
    auxiliary - the auxiliary rod to use
    """
    if n == 1:
        # If there is only one disk, move it directly to the destination rod
        print(f"Move disk 1 from rod {source} to rod {destination}")
        return

    # Move the n-1 smallest disks from the source rod to the auxiliary rod
    tower_of_hanoi(n-1, source, auxiliary, destination)

    # Move the largest disk from the source rod to the destination rod
    print(f"Move disk {n} from rod {source} to rod {destination}")

    # Move the n-1 smallest disks from the auxiliary rod to the destination rod
    tower_of_hanoi(n-1, auxiliary, destination, source)

# Example usage
n = 3  # Number of disks to move
source = "A"  # Source rod
destination = "C"  # Destination rod
auxiliary = "B"  # Auxiliary rod
tower_of_hanoi(n, source, destination, auxiliary)
