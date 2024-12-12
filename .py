def formatar_cpf(cpf):
    # Remove quaisquer espaços extras
    cpf = cpf.strip()
    
    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF inválido! Deve conter exatamente 11 números.")
    
    # Formata o CPF com pontos e traço
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def receber_cpf():
    while True:
        try:
            cpf = input("Digite o CPF (apenas números): ")
            cpf_formatado = formatar_cpf(cpf)
            return cpf_formatado
        except ValueError as e:
            print(e)

# Exemplo de uso
cpf = receber_cpf()
print(f"CPF formatado: {cpf}")
