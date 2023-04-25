<template>
  <div id="app">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <nav >
      <router-link class="p-1 m-1" to="/">Home</router-link> |
      <router-link class="p-1 m-1" to="/page1">PAgina 1</router-link>
      <router-link class="p-1 m-1" to="/page2">PAgina 2</router-link>
      <router-link class="p-1 m-1" to="/login">Logar</router-link>
      <div>{{ logado }}</div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  computed: {
    ...mapGetters(['logado'])
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
