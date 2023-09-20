class Aluno {
  constructor(ra, nome) {
    this.ra = ra;
    this.nome = nome;
  }

  imprimirInfo() {
    console.log(`RA: ${this.ra}`);
    console.log(`Nome: ${this.nome}`);
  }
}

class MeuAluno extends Aluno {
  verificaRA() {
    const meuRA = "N019395";
    if (this.ra === meuRA) {
      console.log("Este RA pertence a você!");
    } else {
      console.log("Este RA não pertence a você.");
    }
  }
}

const raInserido = prompt("Insira seu RA:");
const nomeInserido = prompt("Insira seu nome:");

const meuAluno = new MeuAluno(raInserido, nomeInserido);

meuAluno.imprimirInfo();

meuAluno.verificaRA();
