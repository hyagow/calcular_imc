def calcular_imc(peso, altura):
    # Fórmula do IMC: peso / altura^2
    imc = peso / (altura ** 2)
    return imc

def main():
    while True:
        print("\nCalculadora de IMC")
        print("------------------")
        
        try:
            peso = float(input("Digite seu peso em kg: "))
            altura = float(input("Digite sua altura em metros: "))
            
            if peso <= 0 or altura <= 0:
                raise ValueError("O peso e a altura devem ser valores positivos e diferentes de zero.")
            
            imc = calcular_imc(peso, altura)
            
            print(f"Seu IMC é: {imc:.2f}")
            
            if imc < 18.5:
                print("Você está abaixo do peso.")
            elif imc < 25:
                print("Você está com peso normal.")
            elif imc < 30:
                print("Você está com sobrepeso.")
            else:
                print("Você está obeso.")
                
        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, digite números válidos para peso e altura.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente ou contate o suporte.")
        
        continuar = input("\nDeseja calcular o IMC novamente? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
