<template>
  <v-container fluid>
    <v-data-iterator
      :items="ferramentas"
      :search="search"
      >
     <template v-slot:header >
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
    <template v-if="ferramentas && ferramentas.length" v-slot="ferr">
      <v-row>
        <v-col
          v-for="ferramenta in ferr.items"
          :key="ferramenta.id"
          cols="16"
          sm="12"
          md="6"
          lg="4"
        >
          <v-card elevation="4" class="my-2" dark>
            <v-card-title id="titulo" dark class="text-body-1">{{
              ferramenta.nome
            }}</v-card-title>
            <v-divider></v-divider>
            <v-card-actions class="corpo">
              <template>
                <v-col cols="auto">
                  <v-dialog max-width="600px">
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn text v-bind="attrs" v-on="on">
                        <v-icon small>mdi-pencil</v-icon>
                        EDITAR
                      </v-btn>
                    </template>
                     <template v-slot:default="dialog3">
                      <v-card>
                        <v-card-title>
                          <span class="headline">EDITAR FERRAMENTA</span>
                        </v-card-title>
                        <v-card-text>
                          <v-container>
                            <v-form ref="form" v-model="isValid">
                              <v-text-field
                                label="nome"
                                v-model="ferramenta.nome"
                              >
                              {{ ferramenta.nome }}
                              </v-text-field>
                              <v-text-field
                                label="descrição"
                                v-model="ferramenta.descricao"
                              >
                              {{ ferramenta.descricao }}
                              </v-text-field>
                            </v-form>
                          </v-container>
                        </v-card-text>
                        <v-card-actions>
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog3 = false"> Voltar </v-btn>
                          <v-btn
                            :disabled="!isValid"
                            color="success"
                            text
                            @click="atualizarFerramenta(ferramenta);
                            dialog4 = true"
                          >
                            Atualizar
                          </v-btn>
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
                          Deseja remover ? {{ ferramenta.nome }}
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >voltar</v-btn
                          >
                          <v-btn
                            color="error"
                            @click="deleteFerramenta(ferramenta.id);
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
                          >FERRAMENTA
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog7.value = false">
                            <v-icon>mdi-close-thick</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-card-text>
                          <v-container>
                              <v-text-field
                                label="nome"
                                v-model="ferramenta.nome"
                                disabled
                              >
                                {{ ferramenta.nome }}
                              </v-text-field>
                              <v-text-field
                                label="descrição"
                                v-model="ferramenta.descricao"
                                disabled
                              >
                                {{ ferramenta.descricao }}
                              </v-text-field>
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
  </v-data-iterator> 
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
                @click="cadastrarFerramenta();
                dialog6 = true"
              >
                Cadastrar
              </v-btn>
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
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      search: '',
      ferramentas: "",
      ferramenta: {
        nome: null,
        descricao: null,
      },
      dialog: false,
      dialog4: false,
      dialog5: false,
      dialog6: false,
      isValid: true,
    };
  },
  mounted() {
    this.PegarFerramentas();
  },
  methods: {
    cadastrarFerramenta() {
      const ferramenta = {
        nome: this.ferramenta.nome,
        descricao: this.ferramenta.descricao,
      };
      this.axios
        .post("http://otime-api2.herokuapp.com/ferramentasDeSala/", ferramenta)
        .then(
          (response) =>
            (this.ferramentas = [...this.ferramentas, response.data])
        )
        .catch((error) => console.log(error));
      this.dialog = false;
      this.ferramenta.nome = null;
      this.ferramenta.descricao = null;
    },
    deleteFerramenta(ferramentaId) {
      this.axios
        .delete(
          "http://otime-api2.herokuapp.com/ferramentasDeSala/" +
            ferramentaId +
            "/"
        )
        .then(() => {
          this.ferramentas = this.ferramentas.filter(
            (p) => p.id != ferramentaId
          );
        });
    },
    atualizarFerramenta(ferramenta) {
      console.log(ferramenta);
      this.axios
        .put(
          "http://otime-api2.herokuapp.com/ferramentasDeSala/" +
            ferramenta.id +
            "/",
          {
            nome: ferramenta.nome,
            descricao: ferramenta.descricao,
          }
        )
        .then((response) => {
          this.ferramentas = this.ferramentas.map((s) => {
            if (s.id == ferramenta.id) {
              return response.data;
            } else {
              return s;
            }
          });
        })
        .catch((error) => console.log(error));
    },
     PegarFerramentas(){
      this.axios
      .get("http://otime-api2.herokuapp.com/ferramentasDeSala/")
      .then((response) => (this.ferramentas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    }
  },
};
</script>

<style></style>
