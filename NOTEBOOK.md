# Semana 1

## Objetivos Principais

- Explorar a plataforma atual e compreender, por exemplo, os diferentes fluxos de dados e a camada de segurança.
- Aprendizagem sobre Kubernetes.
- Reunir e organizar documentação relevante (ex.: diagramas) para referência futura.

## Observações Detalhadas

Nesta primeira semana, o foco esteve em compreender a plataforma existente, em particular o percurso dos dados dentro da solução e a própria distribuição de todos os componentes dentro do cluster Kubernetes:

- **Recolha de dados (IoT):** uma parte significativa dos dados tem origem em dispositivos IoT distribuídos pela cidade, mas existem dados provenientes diretamente da rede 5G. Estes dados são enviados para um broker MQTT central, onde ficam disponíveis para consumo interno. Através de um Kafka Connector, a informação é posteriormente encaminhada para o Kafka, possibilitando a sua distribuição de forma escalável e garantindo que múltiplos componentes da plataforma a possam consumir em paralelo.
- **Recolha de dados (APIs públicas):** em paralelo, a plataforma integra também dados provenientes de APIs externas, que são consumidos diretamente no processamento e geração de entidades.
- **Persistência histórica de dados:** para além da gestão em tempo real feita pelo Orion, a plataforma garante a persistência de dados históricos através do FIWARE Cygnus, que atua como conector entre o Orion e diferentes sistemas de armazenamento. No caso em análise, o Cygnus está configurado para enviar e guardar a informação no MongoDB, permitindo conservar séries temporais de entidades e atributos. Esta abordagem assegura não só a consulta retrospetiva de dados, mas também a possibilidade de realizar análises estatísticas e comparativas ao longo do tempo.
- **Camada de segurança:** a plataforma recorre ao FIWARE Keyrock como Identity Manager, responsável pela autenticação e gestão de utilizadores e aplicações. Em conjunto, o Wilma PEP Proxy atua como ponto de entrada para validar tokens e garantir que apenas pedidos autenticados prosseguem para os componentes internos. Para complementar, o AuthzForce fornece mecanismos de autorização avançada, permitindo aplicar políticas de acesso granulares sobre os recursos.

## Tarefas Realizadas

- Mapeamento inicial da arquitetura da plataforma e dos fluxos de dados existentes.
- Análise do percurso dos dados desde a recolha (IoT/5G e APIs públicas) até ao armazenamento e disponibilização.
- Levantamento dos principais componentes FIWARE em uso (Orion, Cygnus, Keyrock, Wilma, AuthzForce).
- Exploração da configuração do cluster Kubernetes e identificação de como os serviços estão distribuídos.
- Recolha e organização de documentação relevante (diagramas, especificações técnicas, configurações).
- Estudo introdutório sobre Kubernetes, incluindo conceitos de deployments, services, namespaces, configmaps, secrets e ingresses. Conclusão de uma certificação introdutória em Kubernetes, disponível [neste ficheiro](assets/certificates/Kubernetes%20for%20the%20Absolute%20Beginners%20-%20Hands-on.pdf).

## Tarefas Não Realizadas

Nenhuma a registar nesta semana.

---

# Trabalho Futuro

- **Revisão bibliográfica:** iniciar um levantamento de literatura sobre Plataformas Urbanas de Dados e iniciativas de cidades inteligentes comparáveis.
