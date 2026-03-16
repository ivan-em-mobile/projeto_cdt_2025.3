
```
# 🚀 Engenharia de Software com Python - Portfólio Completo

Este repositório contém uma coleção de aplicações robustas que demonstram competências em **Lógica de Programação**, **Desenvolvimento de Jogos**, **Segurança de Dados** e **Interfaces Gráficas (GUI)**.

---

## 🛠️ Descrição dos Processos e Tecnologias

### 1. 💾 Persistência de Dados e Gestão (JSON/TXT)
* **Gestor de Tarefas Pro:** Utiliza a biblioteca `json` para ler e escrever dados em um arquivo local. Isso demonstra o ciclo de vida dos dados (CRUD), onde as tarefas são salvas automaticamente ao serem adicionadas ou concluídas.
* **Ranking do Quiz:** Implementação de manipulação de arquivos `.txt` para registrar o histórico de performance dos usuários, utilizando o modo de escrita `append ('a')` para não sobrescrever dados antigos.

### 2. 🔐 Lógica de Criptografia (Zenit Polar)
* **Processamento de Strings:** Desenvolvimento de um algoritmo de substituição de caracteres baseado em dicionários (`Mapas`). 
* **Preservação de Integridade:** O código foi projetado para ignorar caracteres especiais e manter o *case-sensitivity* (diferença entre maiúsculas e minúsculas) durante a cifragem.

### 3. 🎮 Motores de Jogos e Gráficos (Pygame)
* **Tetris Fire Neon:** Focado em algoritmos de renderização de baixo nível (Doom Fire) e lógica de matrizes para peças fantasmagóricas e colisões.
* **Blackjack (21):** Aplicação prática de **Programação Orientada a Objetos (POO)**, onde `Baralho`, `Carta` e `Mão` são classes independentes que interagem entre si.

---

## 🧬 Estrutura Técnica do Código

### 📂 Tratamento de Recursos (Imagens e Ícones)
Para garantir que os programas funcionem como executáveis em qualquer computador, implementamos a lógica de **Caminho Absoluto Dinâmico**:

```python
def recurso_path(relative_path):
    """ Resolve caminhos para scripts e executáveis PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

```

### 🎨 Algoritmo de Estabilidade Visual

No projeto Tetris, os cálculos de gradiente de fogo utilizam uma **Paleta Segura**, prevenindo o erro de estouro de bits (quando um valor RGB tenta assumir mais que 255):

* **Solução:** `cor = min(calculo, 255)`

---

## 📦 Como Executar os Projetos

| Projeto | Comando de Execução | Tecnologia Principal |
| --- | --- | --- |
| **Tetris Neon** | `python tetris_neon.py` | Pygame |
| **Blackjack** | `python blackjack.py` | Pygame |
| **Todo List** | `python gestor_tarefas.py` | Tkinter + JSON |
| **Cifrador** | `python zenit_polar.py` | Tkinter |
| **Quiz** | `python quiz_esportivo.py` | Tkinter |

---

## 👨‍💻 Autor

Desenvolvido por **Ivan Silva Jovens do Código da Transformação 2025.3**.


---

**Precisa que eu adicione mais alguma seção específica, como uma tabela de cores dos temas ou os erros específicos de Git que corrigimos?**

```
