 <template>
  <v-container>
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
      <template v-if="$vuetify.breakpoint.mdAndUp">
        <v-spacer></v-spacer>
        <v-btn-toggle v-model="sortDesc" mandatory>
          <v-btn large depressed color="grey" :value="false">
            <v-icon color="#fff">mdi-arrow-up</v-icon>
          </v-btn>
          <v-btn large depressed color="grey" :value="true">
            <v-icon color="#fff">mdi-arrow-down</v-icon>
          </v-btn>
        </v-btn-toggle>
      </template>
    </v-toolbar>
    <template v-if="professores && professores.length">
      <v-row>
        <v-col
          v-for="professor in professores"
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
                    <template v-slot:default="dialog3">
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
                          <v-btn text @click="dialog3.value = false"
                            >VOLTAR</v-btn
                          >
                          <v-btn
                            color="success"
                            text
                            @click="atualizarProfessor(professor.id, professor)"
                            >ATUALIZAR</v-btn
                          >
                        </v-card-actions>
                      </v-card>
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
                          Deseja remover ? {{ professor.nome }}
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >voltar</v-btn
                          >
                          <v-btn
                            color="error"
                            @click="deleteProfessor(professor.id)"
                            >REMOVER</v-btn
                          >
                        </v-card-actions>
                      </v-card>
                    </template>
                  </v-dialog>
                </v-col>
              </template>
              <!------------------------------------------------FIM-REMOVER--------------------------------------------->
              <v-btn text>
                <v-icon small>mdi-format-list-bulleted-square</v-icon>detalhes
              </v-btn>
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
                @click="cadastrarProfessor()"
                >Cadastrar</v-btn
              >
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
      professores: null,
      professor: {
        nome: null,
        abreviatura: null,
        coordenador: false,
      },
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api2.herokuapp.com/professores/")
      .then((response) => (this.professores = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
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
        .then((response) => (this.professores = response.data))
        .catch((error) => console.log(error));
      this.axios
        .get("http://otime-api2.herokuapp.com/professores/")
        .then((response) => (this.professores = response.data))
        .catch((error) => console.log("Erro na requisição GET: " + error));
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
  },
};
</script>
<style>
</style>