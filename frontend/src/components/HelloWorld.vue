<template>
  <v-container class="otime">
    <v-row class="text-center ">
      <v-col>
        <h1 class="display-2 font-weight-bold mb-3">O'Time</h1>
        <h3>Gerenciador de horários escolares</h3>
      </v-col>
      <v-col cols="12">
        <v-row justify="center">
          <div id="app">
              <div class="text-center">
                <v-dialog v-model="dialog" width="500">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn elevation="12" color="blue" dark v-bind="attrs" v-on="on" class="saibaMais" >SAIBA MAIS</v-btn>
                  </template>

                  <v-card>
                    <v-card-title class="headline grey lighten-2">Saiba mais</v-card-title>
                    <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</v-card-text>
                    <v-divider></v-divider>

                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="error" text @click="dialog = false">Fechar</v-btn>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </div>
          </div>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<style>
.otime {
    height: 10em;
    position: relative }
.otime  {
    margin: 0;
    position: absolute;
    top: 40%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%) }
</style>

<script>
export default {
  data() {
    return {
      dialog: false,
    };
  },
};
</script>