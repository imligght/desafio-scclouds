# Questões Conceituais

##### 1 - Diferenciar as camadas 2 e 3 do modelo OSI, e indicar os protocolos utilizados para endereçamento nestas camadas.

**Resposta:** O modelo OSI é (Open System Interconnection) é uma estrutura teórica dividida em camadas (sete camadas) desenvolvida para padronizar as funções de comunicação de sistemas de computação sem depender de suas estruturas internas e tecnologias específicas. Na sequência, darei uma breve explicação sobre as camadas 3 e 2 e destacarei suas principais diferenças:

## Camada 3: camada de rede
A camada de rede é encarregada de viabilizar a transferência de dados entre redes distintas. Quando dois dispositivos estão se comunicando dentro da mesma rede, a função dessa camada torna-se desnecessária. No dispositivo remetente, a camada de rede fragmenta os segmentos provenientes da camada de transporte em menores unidades chamadas pacotes, e no dispositivo receptor, ela recompõe esses pacotes. Além disso, a camada de rede determina a rota física mais eficiente para que os dados alcancem seu destino, processo conhecido como roteamento.

## Camada 2: camada de enlace de dados
A camada de enlace de dados é bastante parecida com a camada de rede, com a diferença de que ela facilita a transferência de dados entre dois dispositivos dentro da mesma rede. Essa camada recebe os pacotes da camada de rede e os fragmenta em unidades menores chamadas "quadros". Assim como a camada de rede, a camada de enlace de dados também gerencia o controle de fluxo e o controle de erros durante a comunicação dentro da rede.

## Diferenças entre a camada de rede e a camada de enlace de dados
Agora que já temos uma ideia do que se trata cada uma das camadas, podemos agora focar em suas diferenças. Apesar de serem duas camadas relativamente parecidas, elas têm suas diferenças. Sendo as principais delas:

1. **Escopo:** Podemos dizer que a camada de enlace de dados e a camada de rede trabalham em escopos diferentes. Pois, enquanto a camada de rede opera possibilitando a comunicação entre duas redes diferentes, a camada de enlace de dados trabalha facilitando a comunicação entre dispositivos que residem na mesma rede, isto é, dispositivos que estejam dentro de uma mesma rede local (LAN).

2. **Endereçamento:** As camadas de rede e de enlace de dados utilizam métodos de endereçamento difrerentes. A camada de rede utiliza endereçamento IP (Internet Protocol) para identificar a origem e o destino de dados. A camada de enlace de dados, por sua vez, utiliza endereçamento MAC (Media Access Control) para identificação dos dispositivos.

3. **Dispositivos:** Dispositivos diferentes requerem funções diferentes. Dispositivos que tiram vantagem da camada de enlace de dados são switches e bridges, por exemplo. Enquanto na camada de rede temos os famosos roteadores.

4. **Unidade de dados:** As camadas dois e três trabalham com diferentes unidades de dados. Enquanto a camada de enlace de dados trabalha com quadros (ou frames), a camada de rede trabalha com pacotes (ou packets).

5. **Funções:** Embora ambas as camadas estejam ambas as camadas (camada de rede e de enlace de dados) estejam envolvidas na comunicação entre dispositivos, suas funções são essencialmente diferentes.
### **5.1.** **Funções da camada de rede:**
- **Roteamento:** Determina o caminho que os pacotes devem seguir para alcançar seu destino final através de redes diferentes.
- **Endereçamento lógico:** Utiliza endereços IP para identificar de forma única dispositivos em redes diferentes e permitir o roteamento entre eles.
- **Fragmentação e reassembly:** Divide pacotes grandes em fragmentos menores quando necessário. Reagrupa esses fragmentos no destino final.
- **Controle de tráfego:** Implementa políticas de Qualidade de Serviço (QoS) a fim de garantir a eficiência no roteamento.
- **Gerenciamento de conexões:** Utiliza protocolos de roteamento para trocar informações de roteamento entre dispositivos e ajustar dinamicamente os caminhos.

### **5.2** **Funções da camada de enlace de dados:**
- **Controle de acesso ao meio (MAC):** Define regras para quando e como dispositivos podem acessar o meio físico de transmissão para evitar colisões.
- **Detecção e correção de erros:** Utiliza técnicas como a verificação de redundância cíclica (CRC) para detectar e corrigir erros nos dados transmitidos.
- **Endereçamento físico:** Utiliza endereços MAC para identificar de forma única dispositivos na rede local.
- **Encapsulamento de dados:** Formata os dados em quadros (frames) para transmissão na rede local.
- **Fluxo de dados:** Gerencia o fluxo de dados para garantir que o receptor possa processar a informação recebida sem sobrecarga.


### **Protocolos de endereçamento**
**Camada de Rede:** 
- **IPv4 (Internet Protocol version 4) -** Define endereços IP de 32 bits.
- **IPv6 (Internet Protocol version 6) -**  Define endereços IP de 128 bits.
- **ICMP (Internet Control Message Protocol) -** Utilizado para enviar mensagens de controle e erro.
- **ARP (Address Resolution Protocol) -** Mapeia endereços IP para endereços MAC, essencial para a comunicação entre as camadas dois e três.
- **RARP (Reverse Address Resolution Protocol) -** Mapeia endereços MAC para endereços IP, usado principalemente em sistemas sem disco.
- **NDP (Neighbor Discovery Protocol) -** Utilizado no IPv6 para funções similares ao ARP no IPv4, além de outras funções como descoberta de roteadores.

**Camada de Enlace de Dados:**
- **Ethernet -** Utiliza endereços MAC para identificar dispositivos na rede local.
- **Wi-Fi -** Também utiliza endereços MAC, porém, para comunicação sem fio.
- **Bluetooth -** Usa endereços MAC para identificar dispositivos Bluetooth.



##### 2 - Qual a diferença entre adotar uma solução proprietária como o sistema operacional Windows quando comparado a adoção de uma solução OpenSource como o sistema operacional Ubuntu? Quais seriam os pontos negativos e positivos de cada abordagem?

**Resposta:** A adoção de soluções proprietárias como o sistema operacional Windows, em comparação com soluções OpenSource como o sistema operacional Ubuntu, envolvem muitos pontos a serem levados em consideração. Ademais, a melhor opção pode ser relativa, dependendo da necessidade específica de cada usuário ou empresa. Os principais pontos a serem levados em consideração estão listados abaixo:

## Solução proprietária

### Pontos positivos

1. **Suporte técnico e atualizações:** Soluções proprietárias, como o Windows, gerealmente oferecem suporte técnico dedicado e atualizações regulares fornecidas pela empresa proprietária, garantindo, dessa forma, um ambiente seguro e estável.

2. **Compatibilidade com softwares:** É comum que o software proprietário seja desenvolvido para ser compatível com uma ampla gama de sistemas e dispositivos, facilitando a integração em diferentes ambientes.

3. **Qualidade e Confiabilidade:** Muitas vezes, o software proprietário é rigorosamente testado e pode oferecer uma experiência de usuário mais refinada e estável.

4. **Segurança percebida:** Empresas de software proprietário investem pesadamente em segurança, o que pode transmitir uma sensação de maior confiança para os usuários.

### Pontos negativos

1. **Custo:** Softwares proprietários geralmente requerem a compra de licenças ou assinaturas, o que pode representar um custo significativo ao longo do tempo.

2. **Falta de flexibilidade:** O codigo fonto não é disponibilizado ao usuário, limitando a capacidade de customização, flexibilidade e adaptação às necessidades específicas de cada um.

3. **Dependência do fornecedor:** O usuário fica dependente do fornecedor para suporte, atualizações, correções de bugs. O que pode ser um problema caso o fornecedor decida descontinuar o produto.

4. **Falta de controle:** O usuário é passivo sobre como o software evolui ou quais recursos e features são adicionandos, removidos ou modificados.

## Solução OpenSource

### Pontos positivos

1. **Custo:** Softwares OpenSource são geralmente gratuitos para download e uso, reduzindo os custos.

2. **Flexibilidade e customização:** O código-fonte é de livre acesso ao usuário, permitindo que o mesmo modifique o software para atender às suas necessidades específicas.

3. **Transparência:** A disponibilidade do código-fonte para o usuário permite revisões e auditorias independentes e maior transparência, podendo aumentar a confiança na segurança e integridade do software.

4. **Comunidade e colaboração:** Há uma forte cultura de colaboração e suporte comunitário, com muitos desenvolvedores contribuindo para o aprimoramento contínuo do software.

### Pontos negativos

1. **Curva de aprendizado:** Pode haver uma curva de aprendizado mais acentuada, especialmente para usuários menos experientes.

2. **Compatibilidade de software:** Nem sempre é garantida a compatibilidade com todos os softwares e dispositivos, exigindo, às vezes, soluções de contorno.

3. **Suporte técnico:** O suporte oficial pode ser limitado em comparação com o do software proprietário, embora muitas vezes a comunidade ativa compense.

4. **Consistência:** A qualidade e a usabilidade de softwares OpenSource podem variar de projeto para projeto, dependendo da maturidade e do nível de desenvolvimento do grupo.

Portanto, na hora de decidir entre utilizar uma solução proprietária ou uma solução OpenSource, é necessário entender as suas necessidades específicas e escolher aquele que mais se encaixa no seu perfil.



##### 3 - O que seria um projeto OpenSource? Como empresas podem adotar tais tecnologias e o que isso acarreta?

**Resposta:** Um projeto OpenSource é um termo na língua inglesa que significa "código aberto". Quando um projeto é OpenSource, isso significa que qualquer um pode ver, usar, modificar e distribuir o projeto por praticamente qualquer motivo. OpenSource é hoje em dia um movimento tecnológico e uma forma de trabalho que vai além da produção de software e é super poderoso porque diminiu as barreiras para adoção do projeto, o que permite às ideias a se espalharem rapidamente. OpenSource é o oposto dos projetos de software proprietário, nos quais os códigos fontes são de propriedade privada de uma empresa.
Empresas podem adotar tecnologias OpenSource de algumas maneiras, como:

1. **Utilização direta:** Empresas podem adotar softwares OpenSource diretamente em seus sistemas. Alguns exemplos podem ser citados como sistemanas operacionais (como Linux), servidores web (Como Apache), bancos de dados (como MySQL), e muitas outras ferramentas e bibliotecas.

2. **Utilização customizada:** Empresas também podem adotar softwares OpenSource em seus sistemas alterando algumas partes de seu código fonte, para que o projeto melhor se aplique às necessidades específicas da empresa.

3. **Contribuição:** Empresas podem até mesmo contribuir para projetos OpenSource, enviando correção de bugs, novos recursos e ferramentas, melhorias de desempenho, etc. Contribuir para a comunidade pode trazer benefícios em termos de reputação e garantir que as mudanças desejadas sejam integradas ao projeto principal.

Ademais, como conclusão, podemos relembrar os seus benefícios já citados neste arquivo anteriormente, como: **Custo** - OpenSource é geralmente gratuito. **Flexibilidade** - projetos OpenSource podem ser modificados para se adequar às necessidades da empresa. Segurança - OpenSource permite que muitos olhos revisem o código, potencialmente identificando e corrigindo erros rapidamente. Porém, também existem desafios na adoção de softwares OpenSource, como:

1. **Suporte e manutenção:** Pode ser necessário investir em uma equipe interna para suporte e manutenção.

2. **Segurança:** Embora a transparência possa aumentar a segurança, também significa que possíveis vulnerabilidades são visíveis para todos, inclusive para pessoas mal intencionadas.

3. **Qualidade variável:** Nem todos os projetos OpenSource têm a mesma qualidade, alguns podem não ser adequados para o uso em produção. Revisão interna pode ser necessária antes de decidir adotar um software OpenSource.

4. **Licenciamento:** É importante entender e cumprir as condições das licenças OpenSource, pois algumas têm requisitos específicos que podem impactar a forma como o software pode ser usado e distribuído.