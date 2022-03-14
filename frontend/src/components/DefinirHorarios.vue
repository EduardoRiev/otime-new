<template>
<div>
  <v-card max-width="800" class="mx-auto my-6">
    <v-toolbar color="#124A63" dark>
      <v-toolbar-title>Selecione o modo de visualização</v-toolbar-title>

      <v-spacer></v-spacer>
    </v-toolbar>

    <v-list>
      <v-list-item link to="/selecao-sala">
        <v-list-item-icon>
          <v-icon color="#124E70">mdi-chair-school</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Salas</v-list-item-title>
          <v-card-subtitle
            >Visualize os horários reservados para cada sala.</v-card-subtitle
          >
        </v-list-item-content>
      </v-list-item>
      <v-divider class="mx-4"></v-divider>

      <v-list-item link to="selecao-disciplina">
        <v-list-item-icon>
          <v-icon color="#124E70">mdi-book-outline</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Disciplinas </v-list-item-title>
          <v-card-subtitle
            >Visualize os locais e horários reservados para cada disciplina.</v-card-subtitle
          >
        </v-list-item-content>
      </v-list-item>
      <v-divider class="mx-4"></v-divider>

      <v-list-item link to="/selecao-professor">
        <v-list-item-icon>
         <v-icon color="#124E70">mdi-human-male-board</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Professores </v-list-item-title>
          <v-card-subtitle
            >Visualize a disponibilidade de horários para cada professor.</v-card-subtitle
          >
        </v-list-item-content>
      </v-list-item>
      <v-divider class="mx-4"></v-divider>

      <v-list-item link to="/selecao-turma">
        <v-list-item-icon>
          <v-icon color="#124E70">mdi-google-classroom</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title> Turmas </v-list-item-title>
          <v-card-subtitle
            >Visualize os locais e horários reservados para cada
            turma.</v-card-subtitle
          >
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-card>
    <!-- BOTÃO DE ADICIONAR -->
      <v-btn
        class="mx-2"
        fab
        dark
        color="green"
        fixed bottom right
        link to="/submissao-reserva"
      >
        <v-icon dark>
          mdi-plus
        </v-icon>
      </v-btn>
  </div>
</template>
<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>