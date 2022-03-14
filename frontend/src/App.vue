<template>
  <v-app>
    <v-navigation-drawer v-model="drawer" app dark flat color="#0A2C40">
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
          <v-list-group prepend-icon="mdi-chair-school" no-action>
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title>Salas</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item link to="/salas">
              <v-list-item-content>
                <v-list-item-title>Salas</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link to="/ferramentas">
              <v-list-item-content>
                <v-list-item-title>Ferramentas</v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link to="/tipos">
              <v-list-item-content>
                <v-list-item-title>Tipos</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>

          <v-list-item link to="/disciplinas">
            <v-list-item-icon>
              <v-icon>mdi-book-outline</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> Disciplinas </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/professores">
            <v-list-item-icon>
              <v-icon>mdi-human-male-board</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> Professores </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/turmas">
            <v-list-item-icon>
              <v-icon>mdi-google-classroom</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> Turmas </v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item link to="/definir-horario">
            <v-list-item-icon>
              <v-icon>mdi-clock</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> Horários </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar app color="white">
      <div class="drawer-bar">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      </div>

      <v-img
        class="logo-bar d-flex justify-center"
        max-height="257"
        max-width="150"
        :src="require('@/static/logo-new.png')"
      />
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<style>
@import "assets/styles/custom.css";
</style>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    drawer: true
  })
};
</script>
<style>
.logo-bar {
  margin-left: 40%;
}
</style>
