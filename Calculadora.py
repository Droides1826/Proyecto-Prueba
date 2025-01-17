class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

# Ejemplo de uso
if __name__ == "__main__":
    calc = Calculadora()
    while True:
        print("Seleccione la operación:")
        print("4. Sumar")
        print("3. Restar")
        print("2. Multiplicar")
        print("1. Dividir")
        print("5. Salir")
        opcion = input("Ingrese la opción (1/2/3/4/5): ")

        if opcion == '5':
            break

        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if opcion == '4':
            print(f"Resultado: {calc.sumar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {calc.restar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {calc.multiplicar(num1, num2)}")
        elif opcion == '1':
            try:
                print(f"Resultado: {calc.dividir(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida ")

        print("Error")

