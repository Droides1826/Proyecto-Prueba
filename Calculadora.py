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
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Ingrese la opción (1/2/3/4/5): ")

        if opcion == '5':
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print(f"Resultado: {calc.sumar(num1, num2)}")
        elif opcion == '2':
            print(f"Resultado: {calc.restar(num1, num2)}")
        elif opcion == '3':
            print(f"Resultado: {calc.multiplicar(num1, num2)}")
        elif opcion == '4':
            try:
                print(f"Resultado: {calc.dividir(num1, num2)}")
            except ValueError as e:
                print(e)
        else:
            print("Opción no válida ")

        print("Hola sdaskjhdkjsahdkjhsajdhsakjdh")

