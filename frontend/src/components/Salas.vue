<template>
  <v-container fluid>
    <v-data-iterator
      :items="salas"
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
    <template v-if="sala && salas.length" v-slot='sal'>
      <v-row>
        <v-col
          v-for="sala in sal.items"
          :key="sala.id"
          cols="16"
          sm="12"
          md="6"
          lg="4"
        >
          <v-card elevation="4" class="my-2" dark>
            <v-card-title id="titulo" dark class="text-body-1">
              {{ sala.nome }}
              </v-card-title>
            <v-card-actions class="corpo">
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
                          >EDITAR SALA
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
                                    v-model="sala.tipos"
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
                        <v-spacer></v-spacer>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false">VOLTAR</v-btn>
                          <v-btn 
                            color="success" 
                            @click="atualizarSala(sala.id, sala);
                            dialog2.value = false;
                            dialog4 = true">ATUALIZAR</v-btn>
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
                          Deseja remover ? {{ sala.nome }}
                        </v-card-text>
                        <v-divider></v-divider>
                        <v-card-actions class="justify-end">
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog2.value = false"
                            >voltar</v-btn
                          >
                          <v-btn 
                            color="error" 
                            @click="deleteSala(sala.id);
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
                          >SALA
                          <v-spacer></v-spacer>
                          <v-btn text @click="dialog7.value = false">
                            <v-icon>mdi-close-thick</v-icon>
                          </v-btn>
                        </v-card-title>
                        <v-card-text>
                          <v-container>
                            <v-text-field
                              label="nome"
                              v-model="sala.nome"
                              disabled
                            ></v-text-field>
                            <v-text-field
                              label="abreviatura"
                              v-model="sala.abreviatura"
                              disabled
                            ></v-text-field>
                            <v-text-field
                              label="capacidade"
                              v-model="sala.capacidade"
                              disabled
                            ></v-text-field>
                            <v-row align="center">
                              <v-col>
                                <v-select
                                  v-model="sala.tipos"
                                  :items="tipos"
                                  item-text="nome"
                                  item-value="id"
                                  label="tipos"
                                  multiple
                                  disabled
                                ></v-select>
                              </v-col>
                            </v-row>
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
                @click="cadastrarSala();
                dialog6 = true"
              >
                Cadastrar
              </v-btn>
            </v-card-actions>
            <v-dialog
              v-model="dialog6"
              max-width="250"
              >
                <v-alert color="success">
                  Cadastro bem sucedido!
                </v-alert>
              </v-dialog>
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
      salas: "",
      sala: {
        nome: null,
        abreviatura: null,
        capacidade: null,
        tipos: [],
      },
      selectedTools: null,
      tipos: null,
      dialog: false,
      dialog4: false,
      dialog5: false,
      dialog6: false,
      isValid: true,
    };
  },
  mounted() {
    this.PegarSalas()
    this.axios
      .get("http://otime-api2.herokuapp.com/tiposDeSala/")
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
        .post("http://otime-api2.herokuapp.com/salas/", sala)
        .then((response) => (this.salas = [...this.salas, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.sala.nome = null;
      this.sala.abreviatura = null;
      this.sala.capacidade = null;
    },
    deleteSala(salaId) {
      this.axios
        .delete("http://otime-api2.herokuapp.com/salas/" + salaId + "/")
        .then(() => {
          this.salas = this.salas.filter((p) => p.id != salaId);
        });
    },
    atualizarSala(salaId, sala) {
      console.log(sala);
      this.axios
        .put("http://otime-api2.herokuapp.com/salas/" + salaId + "/", {
          nome: sala.nome,
          abreviatura: sala.abreviatura,
          capacidade: sala.capacidade,
          tipos: sala.tipos,
        })
        .then((response) => {
          this.salas = this.salas.map((s) => {
            if (s.id == sala.id) {
              console.log("cai no if");
              this.salas = response.data;
              return response.data;
            } else {
              console.log("cai no if");
              return s;
            }
          });
          this.pegarSalas();
        })
        .catch((error) => console.log(error));
    },
    PegarSalas() {
      this.axios
        .get("http://otime-api2.herokuapp.com/salas/")
        .then((response) => (this.salas = response.data))
        .catch((error) => console.log("Erro na requisição GET: " + error));
    }
  },
};
</script>

<style></style>
