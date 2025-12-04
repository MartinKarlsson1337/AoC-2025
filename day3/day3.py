

class Battery:
    def __init__(self, joltage: int):
        self.joltage = joltage
        self.is_on = False  

    def turn_on(self) -> None:
        self.is_on = True

    def turn_off(self) -> None:
        self.is_on = False


class Bank:
    def __init__(self):
        self.batteries = []

    def add_battery(self, battery: Battery) -> None:
        self.batteries.append(battery)

    def total_joltage(self) -> int:
        turned_on_batteries = [str(b.joltage) for b in self.batteries if b.is_on]
        return int("".join(turned_on_batteries))

    def optimize_batteries(self) -> list[Battery]:
        max_joltage = 0
        current_config = []
        for i in range(len(self.batteries)):
            for j in range(i + 1, len(self.batteries)):
                self.batteries[i].turn_on()
                self.batteries[j].turn_on()
                current_total = self.total_joltage()
                if current_total > max_joltage:
                    max_joltage = current_total
                    current_config = [self.batteries[i], self.batteries[j]]
                self.batteries[i].turn_off()
                self.batteries[j].turn_off()

        return current_config

        
            

if __name__ == "__main__":
    with open("./day3/day3.txt", "r") as file:
        data = file.read().strip().splitlines()

    banks = []
    for line in data:
        bank = Bank()
        for joltage in line:
            battery = Battery(int(joltage))
            bank.add_battery(battery)
        banks.append(bank)

    total = 0
    for bank in banks:
        optimal_batteries = bank.optimize_batteries()
        for battery in optimal_batteries:
            battery.turn_on()
        total += bank.total_joltage()

    print("Total Joltage:", total)