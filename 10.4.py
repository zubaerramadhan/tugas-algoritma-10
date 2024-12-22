file_name = input("Masukkan nama file: ")

try:
    with open(file_name, 'r') as file:
        domain_count = {}
        for line in file:
            if line.startswith('dari '):
                email = line.split()[1]
                domain = email.split('@')[1]
                domain_count[domain] = domain_count.get(domain, 0) + 1
        print(domain_count)

except FileNotFoundError:
    print(f"File '{file_name}' tidak ditemukan.")