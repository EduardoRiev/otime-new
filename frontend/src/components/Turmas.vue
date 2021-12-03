<template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title> Turmas </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon> mdi-magnify </v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="turmas && turmas.length">
      <v-card class="my-2" dark v-for="turma in turmas" :key="turma.id">
        <v-card-title>
          {{ turma.nome }}
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn icon>
              <v-icon> mdi-pencil </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card-title>
        <v-card-subtitle>
          {{ turma.abreviatura }}
        </v-card-subtitle>
        <v-card-title> turma #{{ turma.id }} </v-card-title>
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
              <span class="headline">Nova turma</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="turma.nome"
                  ></v-text-field>
                  <v-text-field
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    required
                    label="abreviatura"
                    v-model="turma.abreviatura"
                  ></v-text-field>
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
                @click="cadastrarTurma()"
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
      turmas: null,
      turma: {
        nome: null,
        abreviatura: null,
      },
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/turmas/")
      .then((response) => (this.turmas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    cadastrarTurma() {
      const turma = {
        nome: this.turma.nome,
        abreviatura: this.turma.abreviatura,
      };
      this.axios
        .post("http://otime-api.herokuapp.com/turmas/", turma)
        .then((response) => (this.turmas = [...this.turmas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.turma.nome = null;
      this.turma.abreviatura = null;
    },
  },
};
</script>

<style>
</style>