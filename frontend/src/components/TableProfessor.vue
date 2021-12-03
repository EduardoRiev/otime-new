<template>
  <div>
    <h1>Professor: {{ professor.nome }}</h1>
    <v-data-table
      :headers="headers"
      :items="horarios"
      :items-per-page="12"
      hide-default-footer
      class="elevation-1"
    ></v-data-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      professor: {},
      horarios: [],
      headers: [
        { text: "Horário", value: "0" },
        { text: "Segunda-feira", value: "1" },
        { text: "Terça-feira", value: "2" },
        { text: "Quarta-feira", value: "3" },
        { text: "Quinta-feira", value: "4" },
        { text: "Sexta-feira", value: "5" },
      ],
    };
  },
  mounted() {
    const horariosMap = {
      1: "7:00 - 7:45",
      2: "7:45 - 8:30",
      3: "8:50 - 9:35",
      4: "9:35 - 10-20",
      5: "10:30 - 11:15",
      6: "11:15 - 12:00",
      7: "13:00 - 13:45",
      8: "13:45 - 14:30",
      9: "14:50 - 15:35",
      10: "15:35 - 16:20",
      11: "16:30 - 17:15",
      12: "17:15 - 18:00",
    };

    var professorId = this.$route.params.id;

    function criarMap(arrayDados) {
      var resultado = {};

      arrayDados.forEach((dado) => {
        resultado[dado.id] = dado;
      });

      return resultado;
    }

    var montarTabelaHorario = () => {
      console.log("cards", this.cards);
      var horarios = { 1: {}, 2: {}, 3: {}, 4: {}, 5: {} };

      this.cards.forEach((card) => {
        horarios[card.dia][card.horario] = card;
      });

      var horarioTable = [];

      for (let h = 1; h <= 12; h++) {
        var horarioLinha = [horariosMap[h]];
        for (let dia = 1; dia <= 5; dia++) {
          var card = horarios[dia][h];

          if (card) {
            var disciplina = this.disciplinas[card.disciplina];
            var professor = this.professores[disciplina.professores[0]];
            var turma = this.turmas[card.turma];

            var horarioItem = `
              ${disciplina.nome} - 
              ${turma.nome} - 
              ${professor.nome}`;

            console.log("table Item", horarioItem);

            horarioLinha.push(horarioItem);
          } else {
            horarioLinha.push(null);
          }
        }

        horarioTable.push(horarioLinha);
      }
      console.table(horarioTable);
      this.horarios = horarioTable;
    };

    this.axios
      .get("http://otime-api.herokuapp.com/cards/", {
        params: {
          professor: professorId,
        },
      })
      .then((response) => {
        this.cards = response.data;
        this.axios
          .get("http://otime-api.herokuapp.com/disciplinas/")
          .then((response) => {
            this.disciplinas = criarMap(response.data);
            this.axios
              .get("http://otime-api.herokuapp.com/turmas/")
              .then((response) => {
                this.turmas = criarMap(response.data);
                this.axios
                  .get("http://otime-api.herokuapp.com/salas/")
                  .then((response) => {
                    this.professores = criarMap(response.data);
                    this.axios
                      .get("http://otime-api.herokuapp.com/professores/" + professorId + "/")
                      .then((response) => {
                        this.professor = response.data;
                        montarTabelaHorario();
                      })
                      .catch((error) =>
                        console.log("Error na requisição GET:", error)
                      );
                  })
                  .catch((error) =>
                    console.log("Error na requisição GET:", error)
                  );
              })
              .catch((error) => console.log("Error na requisição GET:", error));
          })
          .catch((error) => console.log("Error na requisição GET:", error));
      })
      .catch((error) => console.log("Erro na requisição GET:", error));
  },
};
</script>
