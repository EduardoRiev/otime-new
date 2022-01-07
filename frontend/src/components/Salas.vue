<template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title> Salas </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon> mdi-magnify </v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="salas && salas.length">
      <v-card class="my-2" dark v-for="sala in salas" :key="sala.id">
        <v-card-title>
          {{ sala.nome }}
          <v-spacer></v-spacer>
          <v-card-actions>
            <v-btn icon>
              <v-icon> mdi-pencil </v-icon>
            </v-btn>
          </v-card-actions>
        </v-card-title>
        <v-card-subtitle>
          {{ sala.abreviatura }}
        </v-card-subtitle>
        <v-card-title> sala #{{ sala.id }} </v-card-title>
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
                      Deseja remover ? {{ sala.nome }}
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions class="justify-end">
                      <v-spacer></v-spacer>
                      <v-btn text @click="dialog2.value = false">voltar</v-btn>
                      <v-btn
                        color="error"
                        @click="deleteSala(sala.id)"
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
              <span class="headline">Nova sala</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="sala.nome"
                  ></v-text-field>
                  <v-text-field
                    label="abreviatura"
                    v-model="sala.abreviatura"
                  ></v-text-field>
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="capacidade"
                    v-model="sala.capacidade"
                  ></v-text-field>
                  <v-row align="center">
                    <v-col>
                      <v-select
                        v-model="selectedTools"
                        :items="tipos"
                        item-text="nome"
                        item-value="id"
                        label="tipos"
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
                @click="cadastrarSala()"
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
      salas: null,
      sala: {
        nome: null,
        abreviatura: null,
        capacidade: null,
      },
      selectedTools: null,
      tipos: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/salas/")
      .then((response) => (this.salas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    this.axios
      .get("http://otime-api.herokuapp.com/tiposDeSala/")
      .then((response) => (this.tipos = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    cadastrarSala() {
      const sala = {
        nome: this.sala.nome,
        abreviatura: this.sala.abreviatura,
        capacidade: this.sala.capacidade,
        tipos: this.selectedTools,
      };
      this.axios
        .post("http://otime-api.herokuapp.com/salas/", sala)
        .then((response) => (this.salas = [...this.salas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.sala.nome = null;
      this.sala.abreviatura = null;
      this.sala.capacidade = null;
    },
    deleteSala(salaId) {
      this.axios
        .delete("http://otime-api.herokuapp.com/salas/" + salaId)
        .then(() => {
          this.salas = this.salas.filter(
            (p) => p.id != salaId
          );
        });
    },
  },
};
</script>

<style></style>
