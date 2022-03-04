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
      <v-card
        class="my-2"
        color="blue-grey darken-3"
        dark
        v-for="turma in turmas"
        :key="turma.id"
      >
        <v-card-title>
          {{ turma.nome }}
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-subtitle>{{ turma.abreviatura }}</v-card-subtitle>
        <v-card-actions>
          <template>
            <v-col cols="auto">
              <v-dialog max-width="600">
                <template v-slot:activator="{ on, attrs }">
                  <v-btn text outlined v-bind="attrs" v-on="on">
                    <v-icon small>mdi-pencil</v-icon>
                    EDITAR
                  </v-btn>
                </template>
                <template v-slot:default="dialog3">
                  <v-card>
                    <v-card-title class="headline">EDITAR TURMA </v-card-title>
                    <v-card-text>
                      <v-container>
                        <v-form ref="form" v-model="isValid">
                          <v-text-field label="nome" v-model="turma.nome">
                            {{ turma.nome }}
                          </v-text-field>
                          <v-text-field
                            label="abreviatura"
                            v-model="turma.abreviatura"
                          >
                            {{ turma.abreviatura }}
                          </v-text-field>
                        </v-form>
                      </v-container>
                    </v-card-text>
                    <v-spacer></v-spacer>
                    <v-card-actions class="justify-end">
                      <v-spacer></v-spacer>
                      <v-btn text @click="dialog3.value = false">VOLTAR</v-btn>
                      <v-btn
                        color="success"
                        @click="atualizarTurma(turma.id, turma)"
                        >ATUALIZAR</v-btn
                      >
                    </v-card-actions>
                  </v-card>
                </template>
              </v-dialog>
            </v-col>
          </template>
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
                      Deseja remover {{ turma.nome }}?
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-card-actions class="justify-end">
                      <v-spacer></v-spacer>
                      <v-btn text @click="dialog2.value = false">voltar</v-btn>
                      <v-btn color="error" @click="deleteTurma(turma.id)"
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
      .get('http://otime-api.herokuapp.com/turmas/')
      .then((response) => (this.turmas = response.data))
      .catch((error) => console.log('Erro na requisição GET: ' + error));
  },
  methods: {
    cadastrarTurma() {
      const turma = {
        nome: this.turma.nome,
        abreviatura: this.turma.abreviatura,
      };
      this.axios
        .post('http://otime-api.herokuapp.com/turmas/', turma)
        .then((response) => (this.turmas = [...this.turmas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.turma.nome = null;
      this.turma.abreviatura = null;
    },
    atualizarTurma(turmaId, turma) {
      this.axios
        .put('http://otime-api.herokuapp.com/turmas/' + turmaId + '/', {
          nome: turma.nome,
          abreviatura: turma.abreviatura,
        })
        .then((response) => (this.turmas = response.data))
        .catch((error) => console.log(error));
    },
    deleteTurma(turmaId) {
      this.axios
        .delete('http://otime-api.herokuapp.com/turmas/' + turmaId)
        .then(() => {
          this.turmas = this.turmas.filter((p) => p.id != turmaId);
        });
    },
  },
};
</script>

<style></style>

