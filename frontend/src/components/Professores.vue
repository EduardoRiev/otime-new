 <template>
  <v-container>
    <v-toolbar>
      <v-toolbar-title>Professores</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>
    <template v-if="professores && professores.length">
      <v-card
        class="my-2"
        color="blue-grey darken-3"
        dark
        v-for="professor in professores"
        :key="professor.id"
      >
        <v-card-title>
          {{ professor.nome }}
          <v-spacer></v-spacer>
        </v-card-title>
        <v-card-subtitle>{{ professor.abreviatura }}</v-card-subtitle>
        <v-card-title>
          Coordenador :
          <v-simple-checkbox
            v-model="professor.coordenador"
            disabled
          ></v-simple-checkbox>
        </v-card-title>
        <v-card-actions>
          <v-btn outlined text> <v-icon small>mdi-pencil</v-icon>editar </v-btn>
          <v-btn outlined text>
            <v-icon small>mdi-delete</v-icon>remover
          </v-btn>
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
      .get("http://otime-api.herokuapp.com/professores/")
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
        .post("http://otime-api.herokuapp.com/professores/", professor)
        .then((response) => (this.professores = [...this.professores, response.data]))
        .catch((error) => console.log(error));
      this.dialog = false;
      this.professor.nome = null;
      this.professor.abreviatura = null;
      this.professor.coordenador = null;
      this.professor.imagem = null;
    },
  },
};
</script>

<style>
</style>
