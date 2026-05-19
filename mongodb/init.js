db = db.getSiblingDB('AtividadesProj');

db.createUser({
  user: "usuario_proj",
  pwd: "senha123",
  roles: [
    {
      role: "readWrite",
      db: "AtividadesProj"
    }
  ]
});


// =========================
// COLEÇÃO EMPREGADOS
// =========================

db.empregados.insertMany([
  {
    nome: "Carlos Silva",
    cargo: "Desenvolvedor",
    email: "carlos@email.com"
  },
  {
    nome: "Ana Souza",
    cargo: "Analista",
    email: "ana@email.com"
  },
  {
    nome: "Marcos Lima",
    cargo: "Gerente",
    email: "marcos@email.com"
  }
]);

db.projetos.insertMany([
  {
    nome: "Sistema Financeiro",
    lider: "Marcos Lima",
    status: "Em andamento"
  },
  {
    nome: "Portal Web",
    lider: "Ana Souza",
    status: "Planejamento"
  },
  {
    nome: "Aplicativo Mobile",
    lider: "Carlos Silva",
    status: "Concluído"
  }
]);

db.atividades.insertMany([
  {
    projeto: "Sistema Financeiro",
    descricao: "Criar módulo de login",
    responsavel: "Carlos Silva",
    status: "Em andamento"
  },
  {
    projeto: "Portal Web",
    descricao: "Modelar banco de dados",
    responsavel: "Ana Souza",
    status: "Pendente"
  },
  {
    projeto: "Aplicativo Mobile",
    descricao: "Implementar interface",
    responsavel: "Carlos Silva",
    status: "Concluído"
  }
]);