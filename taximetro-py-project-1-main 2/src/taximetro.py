# how to calculate the fare 
def calculate_fare(action, seconds):
    rate = 2 if action == 'p' else 5
    return seconds * rate

# a function that returns the total fare
def start_trip():
    total_fare = 0
    while True:
        action = input("Ingrese 'p' para parar, 'm' para moverse, o 'f' para finalizar: ").strip().lower()
        if action == 'f':
            break
        seconds = int(input("¿Cuántos segundos?: "))
        total_fare += calculate_fare(action, seconds)
        print(f"Tarifa actual: {total_fare / 100:.2f} euros")
    return total_fare

def main():
    print("\n🚖 Bienvenido al sistema CLI de Taxi 🚖")
    while True:
        input("\nPresione Enter para iniciar un nuevo viaje...")
        total_fare = start_trip()
        print(f"\n💰 Total a pagar: {total_fare / 100:.2f} euros\n")
        if input("¿Iniciar otro viaje? (y/n): ").strip().lower() != 'y':
            print("¡Adiós! 👋")
            break

if __name__ == "__main__":
    main()


 
