<template>
  <v-card max-width="500" class="mx-auto">
    <v-toolbar color="indigo" dark>
      <v-toolbar-title>Selecione a sala</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list v-for="sala in salas" :key="sala.id">
      <v-list-item link :to="`table-sala/${sala.id}`">
        <v-list-item-content>
          <v-list-item-title v-text="sala.nome"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      salas: null,
      sala: {
        nome: null,
        abreviatura: null,
        capacidade: null,
      },
      selectedTools: null,
      tipos: null,
      dialog: false,
      isValid: true,
    };
  },
  mounted() {
    this.axios
      .get("http://otime-api.herokuapp.com/salas/")
      .then((response) => {
        console.log("salas", response);
        this.salas = response.data;

        console.log("this salas", this.salas);
      })
      .catch((error) => console.log("Erro na requisição GET: " + error));
  },
};
</script>
