<template>
  <v-card max-width="800" class="mx-auto">
    <v-toolbar color="#124A63" dark>
      <v-toolbar-title>Selecione o professor</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list v-for="professor in professores" :key="professor.id">
      <v-list-item link :to="`table-professor/${professor.id}`">
        <v-list-item-content>
          <v-list-item-title v-text="professor.nome"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
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
      .then((response) => {
        console.log("professores", response);
        this.professores = response.data;

        console.log("this professores", this.professores);
      })
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
};
</script>
