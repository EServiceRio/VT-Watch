<template>
  <div id="app">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!--<nav >
      <router-link class="p-1 m-1" to="/">Home</router-link> |
      <router-link class="p-1 m-1" to="/page1">PAgina 1</router-link>
      <router-link class="p-1 m-1" to="/page2">PAgina 2</router-link>
      <router-link class="p-1 m-1" to="/login">Logar</router-link>
      <div>{{ logado }}</div>
    </nav>-->
    <main_menu></main_menu>
    <b-container fluid>
      
      <router-view/>
    </b-container>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import main_menu from '@/components/main_menuComp.vue'
export default {
  computed: {
    ...mapGetters(['logado'])
    },
  components:{
    main_menu
  }
}
</script>

