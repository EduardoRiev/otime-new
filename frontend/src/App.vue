<template>
  <v-app>
    <v-navigation-drawer app dark color="black" flat>
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-img src="https://cdn.vuetifyjs.com/images/john.jpg"></v-img>
          </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
          <v-list-item-content>
            <v-list-item-title class="title">
              Luan C. Redmann
            </v-list-item-title>
            <v-list-item-subtitle class="subtitle">
              Coordenador da Escola do Girafales
            </v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-icon>mdi-account-cog</v-icon>
          </v-list-item-action>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list nav dense>
        <v-list-item-group>
          <v-list-item>
            <v-list-item-icon>
              <v-icon>mdi-magnify</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> buscar </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

           <v-list-group prepend-icon="mdi-chair-school" no-action>
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>salas</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item link to="/salas">
              <v-list-item-content>
                <v-list-item-title>salas</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link to="/ferramentas">
              <v-list-item-content>
                <v-list-item-title>ferramentas</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link to="/tipos">
              <v-list-item-content>
                <v-list-item-title>tipos</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>

          <v-list-item link to="/disciplinas">
            <v-list-item-icon>
              <v-icon>mdi-book-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> disciplinas </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/professores">
            <v-list-item-icon>
              <v-icon>mdi-human-male-board</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> professores </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/turmas">
            <v-list-item-icon>
              <v-icon>mdi-google-classroom</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> turmas </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/definir-horario">
            <v-list-item-icon>
              <v-icon>mdi-clock</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> horários </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar class="d-flex justify-center" app color="black" flat dark>
      <v-toolbar-title class=""><h1 class="title">O'Time</h1></v-toolbar-title>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
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
