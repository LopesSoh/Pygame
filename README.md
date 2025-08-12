# Documentação Bibliotecas Python

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
    - OpenCV 2 com APIs C++ modernizadas, oferecendo melhoria de performance e portabilidade.
- **2015**
    - OpenCV 3.0 adiciona suporte C++11, melhores bindings para Python e mais algoritmos de Machine Learning.
- **2023/2024**
    - OpenCV 4.8.0 traz backend Vulkan (até 4× desempenho), suporte a AVIF/HEVC, OpenVINO e melhorias para JS/Python.
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
    - Depois de ler a imagem ou vídeo, possibilita aplicar operações como:
        - Geométricas
        - Cores
        - Filtros
        - Reconhecimentos
        - Desenhos
- **Exibição ou salvamento do resultado**
    - Possibilita:
        - Mostrar em janelas (`cv2.imshow`)
        - Salvar em disco (`cv2.imwrite`)
        - Exportar como vídeo (`cv2.VideoWriter`)
