<template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title> Ferramentas </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon> mdi-magnify </v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="ferramentas && ferramentas.length">
      <v-card class="my-2" dark v-for="ferramenta in ferramentas" :key="ferramenta.id">
        <v-card-title>
          {{ ferramenta.nome }}
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn icon>
              <v-icon> mdi-pencil </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card-title>
        <v-card-subtitle>
          {{ ferramenta.descricao }}
        </v-card-subtitle>
        <v-card-title> Ferramenta #{{ ferramenta.id }} </v-card-title>
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
              <span class="headline">Nova ferramenta</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="ferramenta.nome"
                  ></v-text-field>
                  <v-text-field
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    required
                    label="descrição"
                    v-model="ferramenta.descricao"
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
                @click="cadastrarFerramenta()"
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
      ferramentas: null,
      ferramenta: {
        nome: null,
        descricao: null,
      },
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/ferramentasDeSala/")
      .then((response) => (this.ferramentas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    cadastrarFerramenta() {
      const ferramenta = {
        nome: this.ferramenta.nome,
        descricao: this.ferramenta.descricao,
      };
      this.axios
        .post("http://otime-api.herokuapp.com/ferramentasDeSala/", ferramenta)
        .then((response) => (this.ferramentas = [...this.ferramentas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.ferramenta.nome = null;
      this.ferramenta.descricao = null;
    },
  },
};
</script>

<style>
</style>
