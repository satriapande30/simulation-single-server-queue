import random
from prettytable import PrettyTable

# Fungsi untuk menghasilkan interarrival time dengan probabilitas tertentu
def generate_interarrival_time():
    probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_number = random.random()
    
    for i in range(len(cumulative_probabilities)):
        if random_number <= cumulative_probabilities[i]:
            return i + 1  # Interarrival time is 1-indexed

# Fungsi untuk menghasilkan service time dengan probabilitas tertentu
def generate_service_time():
    probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_number = random.random()
    
    for i in range(len(cumulative_probabilities)):
        if random_number <= cumulative_probabilities[i]:
            return i + 1  # Service time is 1-indexed

# Fungsi untuk melakukan simulasi antrian
def simulate_queue(num_customers):
    arrival_times = []
    interarrival_times = []
    service_times = []
    service_begin_times = []
    waiting_times = []
    service_end_times = []
    time_in_system = []
    idle_time = 0
    
    for i in range(num_customers):
        if i == 0:
            interarrival_times.append(0)
            arrival_times.append(0)
            service_end_times.append(0)
        else:
            # Menghasilkan interarrival time untuk pelanggan
            interarrival_time = generate_interarrival_time()
            interarrival_times.append(interarrival_time)
            arrival_times.append(arrival_times[i-1] + interarrival_time)
        
        # Menghasilkan service time untuk pelanggan
        service_time = generate_service_time()
        service_times.append(service_time)
        
        if arrival_times[i] >= service_end_times[i-1]:
            service_begin_time = arrival_times[i]
        else:
            service_begin_time = service_end_times[i-1]
            idle_time += service_begin_time - arrival_times[i]
        
        service_begin_times.append(service_begin_time)
        waiting_time = max(0, service_begin_time - arrival_times[i])
        waiting_times.append(waiting_time)
        service_end_time = service_begin_time + service_time
        service_end_times.append(service_end_time)
        time_in_system.append(service_end_time - arrival_times[i])
    
    # Menghitung total waktu antrean, total waktu pelayanan, dan total waktu di sistem
    total_waiting_time = sum(waiting_times)
    total_service_time = sum(service_times)
    total_time_in_system = sum(time_in_system)
    
    # Menghitung rata-rata waktu antrean
    average_waiting_time = total_waiting_time / num_customers
    
    # Menghitung probabilitas pelanggan dalam antrean
    probability_customer_in_queue = total_waiting_time / (total_service_time + total_waiting_time)
    
    # Menghitung persentase waktu server tidak aktif (idle)
    idle_percentage = (idle_time / service_end_times[-1]) * 100
    
    # Menghitung rata-rata waktu pelayanan
    average_service_time = total_service_time / num_customers
    
    # Menghitung rata-rata panjang antrian bagi orang yang mengantri
    average_queue_length_per_customer = total_waiting_time / num_customers
    
    # Menghitung rata-rata lama pelanggan di sistem
    average_time_in_system = total_time_in_system / num_customers
    
    # Menyimpan hasil simulasi dalam bentuk dictionary
    simulation_results = {
        "arrival_times": arrival_times,
        "interarrival_times": interarrival_times,
        "service_times": service_times,
        "service_begin_times": service_begin_times,
        "waiting_times": waiting_times,
        "service_end_times": service_end_times,
        "time_in_system": time_in_system,
        "idle_time": idle_time,
        "average_waiting_time": average_waiting_time,
        "probability_customer_in_queue": probability_customer_in_queue,
        "idle_percentage": idle_percentage,
        "average_service_time": average_service_time,
        "average_queue_length_per_customer": average_queue_length_per_customer,
        "average_time_in_system": average_time_in_system
    }
    
    return simulation_results

# Fungsi untuk menampilkan hasil simulasi dalam bentuk tabel
def display_results_table(simulation_results):
    num_customers = len(simulation_results["arrival_times"])
    
    # Membuat objek tabel
    table = PrettyTable()
    
    # Menambahkan kolom-kolom ke tabel
    table.field_names = ["Customer", "Interarrival Time", "Arrival Time", "Service Time",
                         "Service Begin Time", "Waiting Time in Queue", "Service End Time",
                         "Time Spent in System"]
    
    # Mengisi data ke dalam tabel
    for i in range(num_customers):
        table.add_row([i + 1, simulation_results["interarrival_times"][i],
                       simulation_results["arrival_times"][i], simulation_results["service_times"][i],
                       simulation_results["service_begin_times"][i], simulation_results["waiting_times"][i],
                       simulation_results["service_end_times"][i], simulation_results["time_in_system"][i]])
    
    # Menampilkan tabel
    print(table)
    
    # Menampilkan informasi tambahan
    print(f"\nTotal idle time of the server: {simulation_results['idle_time']}")
    print(f"Average Waiting Time in Queue: {simulation_results['average_waiting_time']}")
    print(f"Probability of a Customer in Queue: {simulation_results['probability_customer_in_queue']}")
    print(f"Idle Percentage: {simulation_results['idle_percentage']}%")
    print(f"Average Service Time: {simulation_results['average_service_time']}")
    print(f"Average Queue Length per Customer: {simulation_results['average_queue_length_per_customer']}")
    print(f"Average Time a Customer Spends in the System: {simulation_results['average_time_in_system']}")

if __name__ == "__main__":
    num_customers = int(input("Enter the number of customers (1-100): "))
    # Panggil fungsi untuk melakukan simulasi antrian
    simulation_results = simulate_queue(num_customers)
    
    # Menampilkan hasil dalam bentuk tabel
    display_results_table(simulation_results)
