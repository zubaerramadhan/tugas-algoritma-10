file_name = input("Masukkan nama file: ")

try:
    with open(file_name, 'r') as file:
        email_count = {}
        for line in file:
            if line.startswith('dari '):
                words = line.split()
                if len(words) > 1:
                    email = words[1]
                    email_count[email] = email_count.get(email, 0) + 1
        print(email_count)

except FileNotFoundError:
    print(f"File '{file_name}' tidak ditemukan.")