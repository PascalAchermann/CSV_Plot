import sys
import csv
import matplotlib.pyplot as plt

def read_csv_file(file_path):
    """Liest CSV und gibt Header + Daten zurück"""
    with open(file_path, 'r', newline='\n') as f:
        reader = csv.reader(f)
        header = None
        data = []
        for row in reader:
            if len(row) == 0:
                continue
            if row[0].strip().startswith('#'):
                continue
            if header is None:
                header = [h.strip() for h in row]  # erste Zeile = Header
                continue
            data.append([float(x) for x in row])
    return header, data

def generate_picture(des_path, header, data):
    """Erstellt Plot aus CSV-Daten und speichert PNG"""
    if not data:
        print("Keine Daten zum Plotten!")
        return

    x = [row[0] for row in data]  # erste Spalte = x
    num_columns = len(data[0])

    for col in range(1, num_columns):
        y = [row[col] for row in data]
        label = header[col] if header and col < len(header) else f'Column {col}'
        plt.plot(x, y, label=label)

    # Achsenbeschriftung und Titel
    plt.xlabel(header[0] if header else 'X')
    plt.ylabel('Values')
    plt.title('CSV Plot')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(des_path)
    print(f"Plot gespeichert: {des_path}")
    plt.close()

def main():
    if len(sys.argv) < 3:
        print("\n"+"---"*20+"\nUsage:\t\tpython3 plot_csv.py <source_csv> <destination_png>\n" \
        "Condition:\tHeader available on row [0]\n" \
        "\t\tX-Axis on col[0]")
        sys.exit(1)

    src = sys.argv[1]
    des = sys.argv[2]

    header, data = read_csv_file(src)
    generate_picture(des, header, data)

if __name__ == "__main__":
    main()