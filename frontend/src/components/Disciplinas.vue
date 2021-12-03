<template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title> Disciplinas </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon> mdi-magnify </v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="disciplinas && disciplinas.length">
      <v-card class="my-2" dark v-for="disciplina in disciplinas" :key="disciplina.id">
        <v-card-title>
          {{ disciplina.nome }}
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn icon>
              <v-icon> mdi-pencil </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card-title>
        <v-card-subtitle>
          {{ disciplina.abreviatura }}
        </v-card-subtitle>
        <v-card-title> disciplina #{{ disciplina.id }} </v-card-title>
      </v-card>
    </template>
    <template>
      <v-row justify="center">
        <v-dialog v-model="dialog" persistent max-width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="primary"
              dark
              v-bind="attrs"
              v-on="on"
              fixed
              bottom
              right
              fab
            >
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">Nova disciplina</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="disciplina.nome"
                  ></v-text-field>
                  <v-text-field
                    label="abreviatura"
                    v-model="disciplina.abreviatura"
                  ></v-text-field>
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="créditos"
                    v-model="disciplina.creditos"
                  ></v-text-field>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectedTeacher"
                        :items="professores"
                        item-text="nome"
                        item-value="id"
                        label="professoress"
                        multiple
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectedPlaces"
                        :items="salas"
                        item-text="nome"
                        item-value="id"
                        label="locais"
                        multiple
                      ></v-select>
                    </v-col>
                  </v-row>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="dialog = false"> Voltar </v-btn>
              <v-btn
                :disabled="!isValid"
                color="success"
                text
                @click="cadastrarDisciplina()"
              >
                Cadastrar
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-row>
    </template>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      disciplinas: null,
      disciplina: {
        nome: null,
        abreviatura: null,
        creditos: null,
      },
      selectedTeacher: null,
      selectedPlaces: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/disciplinas/")
      .then((response) => (this.disciplinas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api.herokuapp.com/professores/")
      .then((response) => (this.professores = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api.herokuapp.com/salas/")
      .then((response) => (this.salas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    cadastrarDisciplina() {
      const disciplina = {
        nome: this.disciplina.nome,
        abreviatura: this.disciplina.abreviatura,
        credito:  this.disciplina.creditos,
        professores: this.selectedTeacher,
        locais: this.selectedPlaces
      };
      this.axios
        .post("http://otime-api.herokuapp.com/disciplinas/", disciplina)
        .then((response) => (this.disciplinas = [...this.disciplinas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.disciplina.nome = null;
      this.disciplina.abreviatura = null;
      this.disciplina.creditos = null;
    },
  },
};
</script>

<style>
</style>
