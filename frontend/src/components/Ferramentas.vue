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
        <v-card-actions>
          <v-btn outlined text> <v-icon small>mdi-pencil</v-icon>editar </v-btn>
          <!------------------------------------------------REMOVER------------------------------------------------>
          <template>
            <v-col cols="auto">
              <v-dialog max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn text outlined v-bind="attrs" v-on="on">
                    <v-icon small>mdi-delete</v-icon>
                    REMOVER
                  </v-btn>
                </template>
                <template v-slot:default="dialog2">
                  <v-card>
                    <v-card-title class="text-h5 red white--text lighten-2"
                      >EXCLUIR</v-card-title
                    ><v-card-text></v-card-text>
                    <v-card-text class="text-md-body-1 black--text">
                      Deseja remover ? {{ ferramenta.nome }}
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions class="justify-end">
                      <v-spacer></v-spacer>
                      <v-btn text @click="dialog2.value = false">voltar</v-btn>
                      <v-btn
                        color="error"
                        @click="deleteFerramenta(ferramenta.id)"
                        >REMOVER</v-btn
                      >
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-col>
          </template>
          <!------------------------------------------------FIM-REMOVER--------------------------------------------->
          <v-btn outlined text>
            <v-icon small>mdi-format-list-bulleted-square</v-icon>detalhes
          </v-btn>
        </v-card-actions>
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
    deleteFerramenta(ferramentaId) {
      this.axios
        .delete("http://otime-api.herokuapp.com/ferramentasDeSala/" + ferramentaId)
        .then(() => {
          this.ferramentas = this.ferramentas.filter(
            (p) => p.id != ferramentaId
          );
        });
    },
  },
};
</script>

<style>
</style>
