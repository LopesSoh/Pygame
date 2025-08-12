# Relatório Bibliotecas Python

---

## 1-Open CV

### O que é?

O Open Source é uma biblioteca open-source para visão computacional e processamento de imagens. Ele possui uma licença na qual permite o usuário utilizar, modificar e distribuir o software.

### **Criador do Open CV**

O Open CV foi criado pela Intel em 1999, onde seu principal desenvolvedor e líder inicial foi o Gary Bradski, que atuava como engenheiro da Intel e também como pesquisador de IA e visão computacional.

Bradski criou visando fornecer uma biblioteca gratuita e otimizada, podendo tanto ser usada pela indústria e pesquisa acadêmica.

### História

- **1999/2000**
    - Intel lança o projeto para uso interno.
- **2006**
    - Versão 1.0 chega ao público.
- **2009**
    - Open CV 2 com APIs C++ modernizadas, oferecendo melhoria de desempenho e portabilidade.
- **2015**
    - Open CV 3.0 adiciona suporte C++11, melhores bindings para Python e mais algoritmos de Machine Learning.
- **2023/2024**
    - Open CV 4.8.0 traz backend Vulkan (até 4× desempenho), suporte a AVIF/HEVC, OpenVINO e melhorias para JS/Python.
- **2025**
    - Versão 4.12.0 liberada com suporte ao C++20, quantização DNN, HALs para RISC-V e Qualcomm, entre outros.
    - OpenCV 5 Alpha (preview) já disponível.

### **Linguagens e Plataformas**

O OpenCV foi projetado para ser multiplataforma. Ele foi escrito nativamente na biblioteca C++, e a biblioteca do OpenCV suporta Windows, Linux, Android, IOS, MacOS, e possui interfaces C++, Python, Java, MATLAB.

### Como Funciona

- **Nível Conceitual**
    - Pega imagens e vídeos como matrizes de pixels.
    - Aplica operações matemáticas e lógicas para extrair informações visuais.
- **Entrada dos Dados**
    - Carrega dados de várias fontes.
- **Processamento da imagem ou vídeo**
    - Após ler a imagem ou vídeo, possibilita aplicar operações como:
        - Geométricas
        - Cores
        - Filtros
        - Reconhecimentos
        - Desenhos
- **Exibição ou salvamento do resultado**
    - Possibilita:
        - Mostrar em janelas (cv2.imshow)
        - Salvar em disco (cv2.imwrite)
        - Exportar como vídeo (cv2.VideoWriter)

### Principais Recursos

- **CORE / IMGPROC**
    - **CORE**: Funções básicas para lidar com imagens.
    - **IMGPROC**: Ajusta e transforma imagens.
- **Objdetect / Tracking**
    - Detecção de faces.
- **Features2D / Calib3D**
    - **Features2D**: Encontra pontos importantes em imagens.
    - **Calib3D**: Trabalha com visão e medições em 3D.
- **ML interno**
    - Conjunto de métodos de aprendizado de máquina para analisar e classificar dados.
- **DNN**
    - Usa redes neurais para reconhecer e identificar objetos em imagens e vídeos.
- **G-API**
    - Ferramenta do OpenCV para criar e acelerar o processamento de imagens de forma mais rápida e organizada.

### Aplicações Reais

- **Automação e robótica**
    - Detecção de obstáculos
    - Fluxo óptico
    - Reconhecimento de sinais de trânsito
- **Medicina**
    - Segmentação de tumores
    - Registro de imagem
    - Pré-processamento DICOM
    - Análise de contraste
- **Segurança e vigilância**
    - Detecção de movimento
    - Reconhecimento facial
    - Alerta automáticos
- **AR/VR**
    - Interface humano-computador
    - Reconstrução 3D
    - Aplicações em drones
    - Aplicações em veículos autônomos

### Pontos Positivos

- **Gratuito e Open Source** – O OpenCV tem código aberto no GitHub, permitindo uso, estudo, modificação e contribuição por qualquer pessoa.
- **Grande Comunidade e Documentação** – Conta com vasta comunidade, muitos tutoriais, fóruns e documentação oficial detalhada que facilitam o aprendizado e solução de problemas.
- **Integração com outras tecnologias** – Suporta várias linguagens e sistemas operacionais, além de integração com frameworks como TensorFlow, PyTorch e outros.
- **Biblioteca rica e completa** – Oferece milhares de funções, indo de filtros simples até redes neurais avançadas.

### Concorrentes no mercado

**1. Pillow (PIL Fork)**

- **Vantagens:** Simples de usar, ótima para manipulação básica de imagens (corte, redimensionamento, filtros), boa integração com Python puro.
- **Desvantagens:** Pouco voltada para visão computacional avançada, não possui recursos nativos para detecção de objetos, faces, etc.

**2. scikit-image**

- **Vantagens:** Baseada em NumPy/SciPy, fácil integração com bibliotecas científicas, boa para processamento e análise de imagens, código limpo.
- **Desvantagens:** Mais lenta em operações pesadas, não é ideal para aplicações em tempo real, menos suporte para hardware acelerado.

**3. Dlib**

- **Vantagens:** Excelente para detecção e reconhecimento facial, suporte a Machine Learning integrado, bem otimizada em C++.
- **Desvantagens:** Pouco flexível fora de aplicações de faces, comunidade menor que a do OpenCV.

### Funções para serem testadas

- Visão Computacional
- Detecção de objetos em Tempo Real
- Segmentação de imagens
- Reconhecimentos de movimentos e gestos
- Reconhecimento facial
- Realidade aumentada
- Execução de várias operações na imagem

---

## 2- NumPy

### O que é?
NumPy é uma biblioteca Python usada para trabalhar com matrizes (arrays). Criada em 2005 por Travis Oliphant, significa *Numerical Python*.  
Permite operações com álgebra linear, transformada de Fourier e matrizes N-dimensionais. É base para bibliotecas como Pandas, Scikit-Learn, SciPy e TensorFlow.

### Características
- Trabalha com arrays N-dimensionais (`ndarray`)  
- Mais rápido e eficiente que listas Python  
- Ideal para dados complexos (imagens, vídeos, machine learning)  
- Memória contínua, aumentando eficiência (“Localidade de Referência”)  

### Vantagens
- Muito mais rápido que listas comuns  
- Operações vetoriais simples e eficientes  
- Compatibilidade com outras bibliotecas científicas  
- Ideal para grandes volumes de dados numéricos

### Desvantagens
- Tipos de dados homogêneos (não mistura tipos na mesma matriz)  
- Manipulação limitada de strings  
- Curva de aprendizado mais íngreme para iniciantes

---

## 3- Pandas

### O que é?
O Pandas é uma biblioteca open source para ciência de dados. É usado para **limpeza**, **tratamento** e **análise exploratória** de dados.

### Pontos positivos
- Sintaxe fácil de entender  
- Ampla documentação e tutoriais  
- Fácil integração com outras bibliotecas (ex: NumPy)  
- Grande comunidade no GitHub

### Pontos negativos
- Alto consumo de memória RAM com grandes volumes de dados  
- Não é ideal para Big Data (pode travar)  
- Para grandes conjuntos, recomenda-se Spark ou Dask

### Estruturas principais
- **Series** – Array unidimensional com índices para identificar registros  
- **DataFrame** – Estrutura bidimensional (tabelas com linhas e colunas) 

---
## 4- Matplotlib & Seaborn
## O que são?

### Matplotlib
Biblioteca Python para visualização de dados por meio de gráficos.  
Geralmente usada com outras bibliotecas, fornece a base gráfica enquanto as demais oferecem funcionalidades adicionais.

### Seaborn
Biblioteca integrada ao Matplotlib que simplifica e torna mais elegante a criação de gráficos, oferecendo estilos prontos e maior facilidade de uso.

---

## Diferenças

### Matplotlib
- Maior controle sobre os dados.  
- Capaz de criar desde gráficos simples até visualizações complexas.  
- Mais opções de personalização.

### Seaborn
- Mais fácil de usar que o Matplotlib.  
- Possui visualização estatística aprimorada, permitindo gráficos complexos com mais praticidade.  
- Melhor estética, com temas de cor integrados.

---

# 5-Tkinter

- **Criador**: John Ousterhout (década de 1980).
- **Pontos Positivos**:
    - Facilidade de aprendizado e compatibilidade multiplataforma.
    - Widgets básicos prontos e suporte a temas.
    - Comunidade ativa e documentação extensa.
- **Pontos Negativos**:
    - Visual datado e widgets limitados para aplicações avançadas.
    - Layouts menos flexíveis e ferramentas de design pouco intuitivas.
- **Fundamentos Básicos**:
    - Exemplo de código: Criação de janela, botões, labels e uso de gerenciadores de layout (**`pack`**, **`grid`**, **`place`**).

---

## 6-PyQt

- *Criador*: Phil Thompson e Riverbank Computing (1998).
- *Pontos Positivos*:
    - Interfaces modernas e multiplataforma.
    - Qt Designer para criação visual de telas.
    - Widgets avançados (tabelas, gráficos) e integração com C++.
- *Pontos Negativos*:
    - Curva de aprendizado íngreme e licença comercial para uso não aberto.
    - Documentação focada em C++ e complexidade para iniciantes.
- *Funcionamento*:
    - Sistema de sinais e slots para eventos, layouts automáticos e suporte a temas.

