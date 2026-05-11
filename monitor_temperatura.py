def monitor_temperatura():
    limite_temperatura = 80
    
    print("=" * 60)
    print("MONITOR DE TEMPERATURA DE SERVIDOR")
    print("=" * 60)
    print(f"Limite de temperatura: {limite_temperatura}°C")
    print("Digite 'sair' para encerrar o monitoramento\n")
    
    while True:
        try:
            entrada = input("Digite a temperatura do servidor (°C): ")
            
            if entrada.lower() == 'sair':
                print("\nMonitoramento encerrado!")
                break
            
            temperatura = float(entrada)
            
            print(f"\nTemperatura lida: {temperatura}°C")
            
            if temperatura > limite_temperatura:
                print("⚠️  ALERTA! Resfriamento ativado!")
                print(f"   Temperatura acima do limite ({temperatura}°C > {limite_temperatura}°C)\n")
            elif temperatura >= limite_temperatura - 5:
                print("⚠️  AVISO! Temperatura próxima ao limite")
                print(f"   Temperatura: {temperatura}°C\n")
            else:
                print("✓ Temperatura normal")
                print(f"   Temperatura: {temperatura}°C\n")
        
        except ValueError:
            print("❌ Erro! Digite um valor numérico válido\n")


if __name__ == "__main__":
    monitor_temperatura()