<template>
  <v-card max-width="800" class="mx-auto">
    <v-toolbar color="#124A63" dark>
      <v-toolbar-title>Selecione a turma</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list v-for="turma in turmas" :key="turma.id">
      <v-list-item link :to="`table-turma/${turma.id}`">
        <v-list-item-content>
          <v-list-item-title v-text="turma.nome"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
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
      .get("http://otime-api2.herokuapp.com/turmas/")
      .then((response) => {
        console.log("turmas", response);
        this.turmas = response.data;

        console.log("this turmas", this.turmas);
      })
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
};
</script>
