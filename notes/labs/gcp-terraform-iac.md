---
tags: [gcp, terraform, iac, cloud, devops]
phase: labs
topic: Infrastructure as Code com Terraform no GCP
status: completed
priority: medium
created: 2026-07-02
updated: 2026-07-02
started: 2026-07-02
completed: 2026-07-02
---

# ☁️ Infrastructure as Code com Terraform (GSP750)

⏱️ ~40 min | 🎯 Google Cloud Arcade Facilitator Program 2026

## Ao final deste lab você será capaz de:
- [x] Criar, modificar e destruir infraestrutura com Terraform
- [x] Gerenciar dependências entre recursos (implícitas e explícitas)
- [x] Usar provisioners para executar comandos locais
- [x] Associar IP estático a uma VM via código

---

## Por que aprendemos isso?

Infraestrutura como Código (IaC) é o padrão da indústria para gerenciar cloud. Em vez de
clicar no console para criar recursos, você escreve arquivos de configuração declarativos
que são versionáveis, repetíveis e auditáveis.

Terraform é a ferramenta IaC mais usada no mercado, suportando múltiplos provedores
(GCP, AWS, Azure, etc.) com uma única linguagem: HCL (HashiCorp Configuration Language).

Aplicações práticas:
- Deploy automatizado de ambientes de desenvolvimento, staging e produção
- Infraestrutura versionada no Git (review de mudanças como código)
- Replicação de ambientes idênticos (evita "mas na minha máquina funciona")

---

## Como aprendemos?

Lab prático **GSP750** no Google Skills Boost usando:
- Cloud Shell (terminal Linux com `gcloud` pré-instalado)
- Editor integrado do Cloud Shell
- `terraform` CLI instalado via repositório HashiCorp
- Conta temporária do Qwiklabs com projeto GCP real

---

## O que fizemos — passo a passo

### Task 1: Build Infrastructure

**Objetivo:** Criar uma VPC no GCP usando Terraform.

Arquivo `main.tf` inicial:

```hcl
terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  project = "qwiklabs-gcp-02-115f7b0132d6"
  region  = "us-east1"
  zone    = "us-east1-c"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
```

Comandos executados:
```bash
terraform init      # Baixa o provider do Google
terraform apply     # Cria a VPC (digitar "yes" para confirmar)
```

Conceitos aprendidos:
- **Terraform block:** declara os providers necessários
- **Provider block:** configura o provedor (GCP, AWS, etc.)
- **Resource block:** define o recurso a ser criado
- **`terraform init`:** baixa plugins, prepara o diretório
- **`terraform apply`:** executa o plano e cria recursos

---

### Task 2: Change Infrastructure

**Objetivo:** Adicionar tags e modificar recursos.

Adicionamos um resource `google_compute_instance` e depois modificamos:

```hcl
resource "google_compute_instance" "vm_instance" {
  name         = "terraform-instance"
  machine_type = "e2-micro"
  tags         = ["web", "dev"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-12"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config { }
  }
}
```

Conceitos aprendidos:
- **`~` (update in-place):** modifica recurso sem recriar (ex: tags)
- **`-/+` (destroy and recreate):** substitui recurso (ex: trocar imagem do disco)
- **`terraform plan`:** mostra o que será alterado sem aplicar
- **`terraform destroy`:** destrói toda infraestrutura gerenciada

---

### Task 3: Create Resource Dependencies

**Objetivo:** Criar IP estático + bucket + segunda VM com dependências.

```hcl
resource "google_compute_address" "vm_static_ip" {
  name = "terraform-static-ip"
}

# Dependência implícita: Terraform descobre que vm_static_ip
# precisa ser criado antes de ser usado no vm_instance
resource "google_compute_instance" "vm_instance" {
  network_interface {
    network = google_compute_network.vpc_network.self_link
    access_config {
      nat_ip = google_compute_address.vm_static_ip.address
    }
  }
}

# Dependência explícita: usamos depends_on quando a relação
# não pode ser inferida pelo Terraform
resource "google_compute_instance" "another_instance" {
  depends_on = [google_storage_bucket.example_bucket]
  # ...
}
```

Comandos:
```bash
terraform plan -out static_ip    # Salva o plano em arquivo
terraform apply "static_ip"      # Aplica plano salvo
```

Conceitos aprendidos:
- **Dependência implícita:** Terraform infere pela interpolação (`google_compute_address.vm_static_ip.address`)
- **Dependência explícita:** `depends_on` para relações que Terraform não consegue detectar
- **`terraform plan -out arquivo`:** salva o plano para aplicar depois de forma idêntica

---

### Task 4: Provision Infrastructure

**Objetivo:** Executar comando local após criar a VM (provisioner).

```hcl
resource "google_compute_instance" "vm_instance" {
  # ...

  provisioner "local-exec" {
    command = "echo ${self.name}: ${self.network_interface[0].access_config[0].nat_ip} >> ip_address.txt"
  }
}
```

Conceitos aprendidos:
- **`provisioner "local-exec"`:** executa comando na máquina local (Cloud Shell)
- **`self`:** referência ao próprio resource dentro do provisioner
- **`terraform taint`:** marca recurso para ser destruído e recriado no próximo apply
- **Provisioners só rodam na criação** — se o recurso já existe, precisa taint/destroy

---

## Glossário de Comandos

| Comando | O que faz |
|---|---|
| `terraform init` | Baixa providers e inicializa backend |
| `terraform plan` | Mostra o plano de mudanças (dry-run) |
| `terraform plan -out arquivo` | Salva o plano em arquivo |
| `terraform apply` | Aplica o plano (cria/altera/destrói) |
| `terraform apply "arquivo"` | Aplica um plano salvo |
| `terraform destroy` | Destrói todos os recursos gerenciados |
| `terraform show` | Mostra estado atual dos recursos |
| `terraform state list` | Lista recursos no estado |
| `terraform taint recurso` | Marca recurso para recreate |

---

## ⚡ Mini-Exercícios
- [ ] 1. Crie um segundo bucket e uma VM que dependa dele (use `depends_on`)
- [ ] 2. Adicione uma firewall rule via Terraform (resource `google_compute_firewall`)
- [ ] 3. Use `terraform plan` para ver o que muda antes de aplicar

---

## 📚 Recursos desta seção
- [GSP750 original](https://www.cloudskillsboost.google/catalog_lab/1070)
- [Documentação Terraform Google Provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [HashiCorp Learn - Terraform GCP](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started)
- [Terraform Cloud GCP Examples](https://github.com/terraform-google-modules)
