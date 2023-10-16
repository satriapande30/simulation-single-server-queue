import random

# Fungsi untuk menghasilkan interarrival time dengan probabilitas tertentu
def generate_interarrival_time():
    # Probabilitas dari interarrival time
    probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
    # Menghitung kumulatif probabilitas
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_number = random.random()
    
    # Menggunakan random number untuk memilih interarrival time sesuai probabilitas
    for i in range(len(cumulative_probabilities)):
        if random_number <= cumulative_probabilities[i]:
            return i + 1  # Interarrival time is 1-indexed

# Fungsi untuk menghasilkan service time dengan probabilitas tertentu
def generate_service_time():
    # Probabilitas dari service time
    probabilities = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
    # Menghitung kumulatif probabilitas
    cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
    random_number = random.random()
    
    # Menggunakan random number untuk memilih service time sesuai probabilitas
    for i in range(len(cumulative_probabilities)):
        if random_number <= cumulative_probabilities[i]:
            return i + 1  # Service time is 1-indexed

# Fungsi untuk melakukan simulasi antrian
def simulate_queue(num_customers):
    # Inisialisasi list untuk menyimpan data simulasi
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
    
    for i in range(num_customers):
        print(f"Customer {i+1}:")
        print(f"  Interarrival Time: {interarrival_times[i]}")
        print(f"  Arrival Time: {arrival_times[i]}")
        print(f"  Service Time: {service_times[i]}")
        print(f"  Service Begin Time: {service_begin_times[i]}")
        print(f"  Waiting Time in Queue: {waiting_times[i]}")
        print(f"  Service End Time: {service_end_times[i]}")
        print(f"  Time Spent in System: {time_in_system[i]}")
        print()

    print(f"Total idle time of the server: {idle_time}")

if __name__ == "__main__":
    # Meminta input jumlah pelanggan
    num_customers = int(input("Enter the number of customers (1-100): "))
    # Memanggil fungsi untuk melakukan simulasi antrian
    simulate_queue(num_customers)
