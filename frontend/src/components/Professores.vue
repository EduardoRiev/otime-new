<template>
  <v-container fluid>
    <v-data-iterator
      :items="professores"
      :search="search"
      hide-default-footer
      >
    <template v-slot:header>
    <v-toolbar color="#FAFAFA" class="mb-1">
      <v-text-field
        v-model="search"
        clearable
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Pesquisar"
      ></v-text-field>
    </v-toolbar>
    </template>
    <template v-slot:default="prof">
      <v-row>
        <v-col
          v-for="professor in prof.items"
          :key="professor.id"
          cols="16"
          sm="12"
          md="6"
          lg="4"
        >
          <v-card elevation="4" class="my-2" dark>
            <v-card-title id="titulo" dark class="text-body-1">{{
              professor.nome
            }}</v-card-title>
            <v-divider></v-divider>
            <v-card-actions class="corpo">
              <!------------------------------------------------EDITAR------------------------------------------------>
              <template>
                <v-col cols="auto">
                  <v-dialog max-width="600">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn text v-bind="attrs" v-on="on">
                        <v-icon small>mdi-pencil</v-icon>
                        EDITAR
                      </v-btn>
                    </template>
                    <template v-slot:default="dialog2">
                      <v-card>
                        <v-card-title class="headline"
                          >EDITAR PROFESSOR</v-card-title
                        >
                        <v-card-text>
                          <v-container>
                            <v-form ref="form" v-model="isValid">
                              <v-text-field
                                required
                                label="nome"
                                v-model="professor.nome"
                              ></v-text-field>
                              <v-text-field
                                required
                                label="abreviatura"
                                v-model="professor.abreviatura"
                              ></v-text-field>
                              <v-checkbox
                                label="coordenador"
                                v-model="professor.coordenador"
                              ></v-checkbox>
                            </v-form>
                          </v-container>
                        </v-card-text>
                        <v-spacer></v-spacer>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >VOLTAR</v-btn
                          >
                          <v-btn
                            color="success"
                            text
                            @click="atualizarProfessor(professor.id, professor);
                            dialog2.value = false;
                            dialog4 = true"
                            >ATUALIZAR</v-btn
                          >
                        </v-card-actions>
                      </v-card>
                      <v-dialog
                        v-model="dialog4"
                        max-width="250"
                        >
                          <v-alert color="success">
                            Atualização bem sucedida!
                          </v-alert>
                        </v-dialog>
                    </template>
                  </v-dialog>
                </v-col>
              </template>
              <!------------------------------------------------FIM-EDITAR--------------------------------------------->
              <!------------------------------------------------REMOVER------------------------------------------------>
              <template>
                <v-col cols="auto">
                  <v-dialog max-width="600">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn text v-bind="attrs" v-on="on">
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
                          Deseja remover {{ professor.nome }}?
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >voltar</v-btn
                          >
                          <v-btn
                            color="error"
                            @click="deleteProfessor(professor.id);
                            dialog5 = true"
                            >REMOVER</v-btn
                          >
                        </v-card-actions>
                      </v-card>
                      <v-dialog
                        v-model="dialog5"
                        max-width="250"
                        >
                          <v-alert color="success">
                            Exclusão bem sucedida!
                          </v-alert>
                        </v-dialog>
                    </template>
                  </v-dialog>
                </v-col>
              </template>
              <!------------------------------------------------FIM-REMOVER--------------------------------------------->
              <template>
                <v-col cols="auto">
                  <v-dialog max-width="600">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn text v-bind="attrs" v-on="on">
                        <v-icon small>mdi-format-list-bulleted-square</v-icon>
                        DETALHES
                      </v-btn>
                    </template>
                    <template v-slot:default="dialog7">
                      <v-card>
                        <v-card-title class="headline"
                          >PROFESSOR
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog7.value = false">
                            <v-icon>mdi-close-thick</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-card-text>
                          <v-container>
                              <v-text-field
                                label="nome"
                                v-model="professor.nome"
                                disabled
                              >
                                {{ professor.nome }}
                              </v-text-field>
                              <v-text-field
                                label="abreviatura"
                                v-model="professor.abreviatura"
                                disabled
                              >
                                {{ professor.abreviatura }}
                              </v-text-field>
                              <v-checkbox
                                label="coordenador"
                                v-model="professor.coordenador"
                                disabled
                              ></v-checkbox>
                          </v-container>
                        </v-card-text>
                      </v-card>
                    </template>
                  </v-dialog>
                </v-col>
              </template>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
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
              <span class="headline">Novo professor</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-form ref="form" v-model="isValid">
                  <v-text-field
                    required
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    label="nome"
                    v-model="professor.nome"
                  ></v-text-field>
                  <v-text-field
                    :rules="[(v) => !!v || 'Precisamos disso :c']"
                    required
                    label="abreviatura"
                    v-model="professor.abreviatura"
                  ></v-text-field>
                  <v-checkbox
                    label="coordenador"
                    v-model="professor.coordenador"
                  ></v-checkbox>
                </v-form>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="dialog = false">Voltar</v-btn>
              <v-btn
                :disabled="!isValid"
                color="success"
                text
                @click="cadastrarProfessor();
                dialog6 = true"
                >Cadastrar</v-btn
              >
            </v-card-actions>
          </v-card>
          <v-dialog
            v-model="dialog6"
            max-width="250"
            >
              <v-alert color="success">
                Cadastro bem sucedido!
              </v-alert>
            </v-dialog>
        </v-dialog>
      </v-row>
    </template>
    </v-data-iterator>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      search: '',
      professores: [],
      professor: {
        nome: null,
        abreviatura: null,
        coordenador: false,
      },
      dialog: false,
      dialog4: false,
      dialog5: false,
      dialog6: false,
      isValid: true,
    };
  },
  mounted() {
    this.PegarProfessores()
  },
  methods: {
    cadastrarProfessor() {
      const professor = {
        nome: this.professor.nome,
        abreviatura: this.professor.abreviatura,
        coordenador: this.professor.coordenador,
        imagem: this.professor.imagem,
      };
      this.axios
        .post("http://otime-api2.herokuapp.com/professores/", professor)
        .then(
          (response) =>
            (this.professores = [...this.professores, response.data])
        )
        .catch((error) => console.log(error));
      this.dialog = false;
      this.professor.nome = null;
      this.professor.abreviatura = null;
      this.professor.coordenador = null;
      this.professor.imagem = null;
    },
    atualizarProfessor(professorId, professor) {
      this.axios
        .put(
          "http://otime-api2.herokuapp.com/professores/" + professorId + "/",
          {
            nome: professor.nome,
            abreviatura: professor.abreviatura,
            coordenador: professor.coordenador,
          }
        )
        .then((response) => {
          this.professore = response.data;
          this.PegarProfessores();
          this.dialog2 = false;
        })
        .catch((error) => console.log(error));
    },
    deleteProfessor(professorId) {
      this.axios
        .delete(
          "http://otime-api2.herokuapp.com/professores/" + professorId + "/"
        )
        .then(() => {
          this.professores = this.professores.filter(
            (p) => p.id != professorId
          );
        });
    },
    PegarProfessores() {
      this.axios
        .get("http://otime-api2.herokuapp.com/professores/")
        .then((response) => (this.professores = response.data))
        .catch((error) => console.log("Erro na requisição GET: " + error));
    }
  },
};
</script>
<style>
</style>