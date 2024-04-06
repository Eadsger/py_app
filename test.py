import requests

# URL base da API
base_url = 'http://localhost:5000'

# Função para imprimir o resultado de uma requisição
def print_response(response):
    print('Status code:', response.status_code)
    print('Response body:', response.json())

# Testes das funcionalidades básicas do CRUD
def test_create_item():
    print("Teste de criação de um novo item:")
    response = requests.post(f'{base_url}/itens', json={'nome': 'Novo item'})
    print_response(response)

def test_list_items():
    print("Teste de listagem de itens:")
    response = requests.get(f'{base_url}/itens')
    print_response(response)

def test_get_item():
    print("Teste de busca de um item específico:")
    response = requests.get(f'{base_url}/itens/1')
    print_response(response)

def test_update_item():
    print("Teste de atualização de um item existente:")
    response = requests.put(f'{base_url}/itens/1', json={'nome': 'Item atualizado'})
    print_response(response)

def test_delete_item():
    print("Teste de exclusão de um item:")
    response = requests.delete(f'{base_url}/itens/1')
    print_response(response)

# Executar os testes
if __name__ == '__main__':
    test_create_item()
    test_list_items()
    test_get_item()
    test_update_item()
    test_delete_item()
