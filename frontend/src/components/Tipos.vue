<template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title> Tipos </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon> mdi-magnify </v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="tipos && tipos.length">
      <v-card class="my-2" dark v-for="tipo in tipos" :key="tipo.id">
        <v-card-title>
          {{ tipo.nome }}
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn icon>
              <v-icon> mdi-pencil </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card-title>
        <v-card-title> tipo #{{ tipo.id }} </v-card-title>
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
              <span class="headline">Novo tipo</span>
            </v-card-title>
            <v-card-text>
              <v-container fluid>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="tipo.nome"
                  >
                  </v-text-field>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectedTools"
                        :items="ferramentas"
                        item-text="nome"
                        item-value="id"
                        label="ferramentas"
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
                @click="cadastrarTipo()"
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
      tipos: null,
      tipo: {
        nome: null,
        abreviatura: null,
        capacidade: null,
      },
      selectedTools: null,
      ferramentas: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/tiposDeSala/")
      .then((response) => (this.tipos = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api.herokuapp.com/ferramentasDeSala/")
      .then((response) => (this.ferramentas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    cadastrarTipo() {
      const tipo = {
        nome: this.tipo.nome,
        ferramentas: this.selectedTools,
      };
      this.axios
        .post("http://otime-api.herokuapp.com/tiposDeSala/", tipo)
        .then((response) => (this.tipos = [...this.tipos, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.tipo.nome = null;
      this.tipo.ferramentas = null;
    },
  },
};
</script>

<style>
</style>
