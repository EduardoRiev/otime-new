<template>
  <v-card max-width="800" class="mx-auto">
    <v-toolbar color="#124A63" dark>
      <v-toolbar-title>Selecione a disciplina</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list v-for="disciplina in disciplinas" :key="disciplina.id">
      <v-list-item link :to="`table-disciplina/${disciplina.id}`">
        <v-list-item-content>
          <v-list-item-title v-text="disciplina.nome"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      disciplinas: null,
      disciplina: {
        nome: null,
        abreviatura: null,
        creditos: null,
      },
      selectedTeacher: null,
      selectedPlaces: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api2.herokuapp.com/disciplinas/")
      .then((response) => {
        console.log("disciplinas", response);
        this.disciplinas = response.data;

        console.log("this disciplinas", this.disciplinas);
      })
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
};
</script>
