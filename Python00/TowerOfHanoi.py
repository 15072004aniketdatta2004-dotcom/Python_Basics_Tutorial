class TowerOfHanoi:
    def __init__(self, n):
        self.n = n

    def solve(self):
        self.hanoi(self.n, 'A', 'B', 'C')

    def hanoi(self, n, source, auxiliary, destination):
        if n == 1:
            print(f"Move disk 1 from {source} to {destination}")
            return
        self.hanoi(n - 1, source, destination, auxiliary)
        print(f"Move disk {n} from {source} to {destination}")
        self.hanoi(n - 1, auxiliary, source, destination)

if __name__ == "__main__":
    n:int = int(input("Enter the number of disks: "))
    tower = TowerOfHanoi(n)
    tower.solve()