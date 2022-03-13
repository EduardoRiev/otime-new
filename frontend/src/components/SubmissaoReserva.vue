 <template>
  <v-container>
    <template>
          <v-card>
            <v-card-title>
              <span class="headline">Submissão de reserva</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                    <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectDisciplina"
                        :items="disciplinas"
                        item-text="nome"
                        item-value="id"
                        label="Disciplina"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectTurma"
                        :items="turmas"
                        item-text="nome"
                        item-value="id"
                        label="Turma"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectSalas"
                        :items="salas"
                        item-text="nome"
                        item-value="id"
                        label="Sala"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row align="center">
                  <v-col>
                  <v-select
                    v-model="selectHorarios"
                    :items="horarios"
                    item-text="nome"
                    item-value="valor"
                    label="Horário"
                    dense
                  ></v-select>
                  </v-col>
                  </v-row>
                  <v-row align="center">
                  <v-col>
                  <v-select
                    v-model="selectDias"
                    :items="dias"
                    item-text="nome"
                    item-value="valor"
                    label="Dia"
                    dense
                  ></v-select>
                  </v-col>
                  </v-row>
                  <v-row align="center">
                  <v-col>
                  <v-select
                    v-model="selectSequencia"
                    :items="itens"
                    item-text="nome"
                    item-value="valor"
                    label="Sequência"
                    dense
                  ></v-select>
                  </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="dialog = false">Voltar</v-btn>
              <v-btn :disabled="!isValid" color="success" text @click="submeterReserva()">Cadastrar</v-btn>
            </v-card-actions>
          </v-card>
    </template>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      cards: null,
      card: {
        disciplinas: null,
      },
      horarios: [
        {
        nome: "7:00 - 7:45",
        valor: 1
        },
        {
        nome: "7:45 - 8:30",
        valor: 2
        },
        {
        nome: "8:50 - 9:35",
        valor: 3
        },
        {
        nome: "9:35 - 10-20",
        valor:4
        },
        {
        nome: "10:30 - 11:15",
        valor:5
        },
        {
        nome: "11:15 - 12:00",
        valor: 6
        },
        {
        nome: "13:00 - 13:45",
        valor: 7
        },
        {
        nome: "13:45 - 14:30",
        valor:8
        },
        {
        nome: "14:50 - 15:35",
        valor: 9
        },
        {
        nome: "15:35 - 16:20",
        valor: 10
        },
        {
        nome: "16:30 - 17:15",
        valor: 11
        },
        {
        nome: "17:15 - 18:00",
        valor: 12
        }
        ],
      dias: [{
        nome: "Segunda-feira",
        valor: 1}, 
        {
        nome: "Terça-feira",
        valor: 2},
        {
        nome:"Quarta-feira",
        valor: 3
        },
        {
        nome: "Quinta-feira",
        valor: 4
        },
        {
        nome: "Sexta-feira",
        valor: 5
        }],
        itens: [{
        nome: "simples",
        valor: 1}, 
        {
        nome: "duplo",
        valor: 2},
        {
        nome:"Terço",
        valor: 3
        },
        {
        nome: "Quarto",
        valor: 4
        },
        {
        nome: "Quinto",
        valor: 5
        },
        {
        nome:"Sexto",
        valor: 6
        }],
      selectDisciplina: null,
      selectTurma: null,
      selectSalas: null,
      selectSequencia: null,
      selectDias:null,
      selectHorarios: null,
      disciplinas: [],
      salas: [],
      turmas: [],
      disponibilidade: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios;
    this.axios
      .get("http://otime-api2.herokuapp.com/cards/")
      .then((response) => (this.cards = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api2.herokuapp.com/disciplinas/")
      .then((response) => (this.disciplinas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api2.herokuapp.com/turmas/")
      .then((response) => (this.turmas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api2.herokuapp.com/salas/")
      .then((response) => (this.salas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    async submeterReserva() {
      const card = {
        disciplina: this.selectDisciplina,
        sala: this.selectSalas,
        turma: this.selectTurma, 
        horario: this.selectHorarios,
        dia: this.selectDias,
        sequencia: this.selectSequencia

      };
      await this.axios
        .get(`http://otime-api2.herokuapp.com/cards/?sala=${card.sala}&disciplina=${card.disciplina}&turma=&dia=${card.dia}&horario=${card.horario}`)
        .then((response) => {
          console.log('response axios', response) 
          this.disponibilidade = response.data}
          )
        .catch((error) => console.log("Erro na requisição GET: " + error));
      console.log("end get", this.disponibilidade)
      if(this.disponibilidade.length == 0){
        this.axios
          .post("http://otime-api2.herokuapp.com/cards/", card)
          .then(
            (response) =>
              (this.cards = [...this.cards, response.data])
          )
          .catch((error) => console.log(error));
        this.dialog = false;
        this.card.disciplina = [];
      }else{
        alert('Conflito de horário!');
      }

    },
  },
};
</script>