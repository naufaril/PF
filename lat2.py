random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi struktur data
float_values = ()
string_values = []
int_values = {}

# Iterasi melalui daftar
for item in random_list:
    if isinstance(item, float):
        # Jika item adalah float, tambahkan ke dalam tuple
        float_values += (item,)
    elif isinstance(item, str):
        # Jika item adalah string, tambahkan ke dalam list
        string_values.append(item)
    elif isinstance(item, int):
        # Jika item adalah integer, pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        int_values[item] = {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

# Cetak hasilnya
print("Float values:", float_values)
print("String values:", string_values)
print("Integer values:", int_values)