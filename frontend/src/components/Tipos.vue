<template>
  <v-container fluid>
    <v-data-iterator
      :items="tipos"
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
    <template v-if="tipo && tipos.length" v-slot="tip">
      <v-row>
        <v-col
          v-for="tipo in tip.items"
          :key="tipo.id"
          cols="16"
          sm="12"
          md="6"
          lg="4"
        >
          <v-card elevation="4" class="my-2" dark>
            <v-card-title id="titulo" dark class="text-body-1">{{
              tipo.nome
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
                    <template v-slot:default="dialog2">
                      <v-card>
                        <v-card-title>
                          <span class="headline">EDITAR TIPO</span>
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
                                    v-model="tipo.ferramentas"
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
                          <v-btn text @click="dialog2.value = false">VOLTAR</v-btn>
                          <v-btn
                            :disabled="!isValid"
                            color="success"
                            text
                            @click="atualizarTipo(tipo.id, tipo)"
                            ,dialog2.value = false
                          >
                            Atualizar
                          </v-btn>
                        </v-card-actions>
                      </v-card>
                    </template>
                  </v-dialog>
                </v-col>
              </template>
              <!------------------------------------------------REMOVER------------------------------------------------>
              <template>
                <v-col cols="auto">
                  <v-dialog max-width="600px">
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
                          Deseja remover ? {{ tipo.nome }}
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >voltar</v-btn
                          >
                          <v-btn color="error" @click="deleteTipo(tipo.id)"
                            >REMOVER</v-btn
                          >
                        </v-card-actions>
                      </v-card>
                    </template>
                  </v-dialog>
                </v-col>
              </template>

              <v-btn text>
                <v-icon small>mdi-format-list-bulleted-square</v-icon>detalhes
              </v-btn>
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
      search:'',
      tipos: "",
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
    this.PegarTipo()
    this.axios
      .get("http://otime-api2.herokuapp.com/ferramentasDeSala/")
      .then((response) => (this.ferramentas = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
  methods: {
    atualizarTipo(tipoId, tipo) {
      console.log(tipo);
      this.axios
        .put("http://otime-api2.herokuapp.com/tiposDeSala/" + tipoId + "/", {
          nome: tipo.nome,
          ferramentas: tipo.ferramentas,
        })
        .then((response) => {
          this.tipos = this.tipos.map((s) => {
            if (s.id == tipo.id) {
              return response.data;
            } else {
              return s;
            }
          });
          this.PegarTipo();
        })
        .catch((error) => console.log(error));
    },
    cadastrarTipo() {
      const tipo = {
        nome: this.tipo.nome,
        ferramentas: this.selectedTools,
      };
      this.axios
        .post("http://otime-api2.herokuapp.com/tiposDeSala/", tipo)
        .then((response) => (this.tipos = [...this.tipos, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.tipo.nome = null;
      this.tipo.ferramentas = null;
    },
    deleteTipo(tipoId) {
      this.axios
        .delete("http://otime-api2.herokuapp.com/tiposDeSala/" + tipoId + "/")
        .then(() => {
          this.tipos = this.tipos.filter((p) => p.id != tipoId);
        });
    },
    PegarTipo(){
      this.axios
      .get("http://otime-api2.herokuapp.com/tiposDeSala/")
      .then((response) => (this.tipos = response.data))
      .catch((error) => console.log("Erro na requisição GET: " + error));
    }
  },
};
</script>

<style></style>
