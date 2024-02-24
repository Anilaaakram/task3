# TASK 1 - Record the yield
def record_yield(herd_size):
    cow_data = {}
    for _ in range(herd_size):
        cow_code = input("Enter the 3-digit identity code of the cow: ")
        yield_data = []
        for _ in range(14):  # Two milkings per day for 7 days
            yield_val = float(input(f"Enter the yield of cow {cow_code} for the day (in litres): "))
            yield_data.append(yield_val)
        cow_data[cow_code] = yield_data
    return cow_data

# TASK 2 - Calculate the statistics
def calculate_statistics(cow_data):
    total_volume = 0
    total_cows = len(cow_data)
    for cow, yields in cow_data.items():
        total_volume += sum(yields)
    average_yield = total_volume / (total_cows * 14)
    return total_volume, average_yield

# TASK 3 - Identify the most productive cow and cows producing low volume of milk
def identify_cows(cow_data):
    most_productive_cow = max(cow_data, key=lambda x: sum(cow_data[x]))
    low_yield_cows = [cow for cow in cow_data if sum(cow_data[cow]) < 12*4]
    return most_productive_cow, low_yield_cows

# Main program
def main():
    herd_size = int(input("Enter the size of the herd: "))
    cow_data = record_yield(herd_size)
    total_volume, average_yield = calculate_statistics(cow_data)
    most_productive_cow, low_yield_cows = identify_cows(cow_data)

    print(f"Total weekly volume of milk for the herd: {total_volume:.0f} litres")
    print(f"Average yield per cow in a week: {average_yield:.0f} litres")
    print(f"The most productive cow this week is {most_productive_cow}")
    print("Cows producing low volume of milk for four or more days this week:", low_yield_cows)

if __name__ == "__main__":
    main()