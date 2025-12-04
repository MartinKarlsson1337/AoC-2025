

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
    
    def optimize_batteries(self, number_of_picks) -> list[Battery]:
        for battery in self.batteries:
            battery.turn_on()

        removals = len(self.batteries) - number_of_picks
        removed = []
        for i in range(removals):
            min_decrease = None
            total = self.total_joltage()
            for battery in self.batteries:
                if battery not in removed:
                    battery.turn_off()
                    current_total = self.total_joltage()
                    decrease = total - current_total
                    if min_decrease is None or decrease < min_decrease:
                        min_decrease = decrease
                        battery_to_remove = battery
                    battery.turn_on()
            battery_to_remove.turn_off()
            removed.append(battery_to_remove)

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
        bank.optimize_batteries(12)
        total += bank.total_joltage()

    print("Total joltage from optimal batteries:", total)