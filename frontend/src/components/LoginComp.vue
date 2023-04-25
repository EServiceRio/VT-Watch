<template>
    <form @submit.prevent="login">
      <label for="username">Nome de usuário:</label>
      <input type="text" name="username" v-model="username">
  
      <label for="password">Senha:</label>
      <input type="password" name="password" v-model="password">
  
      <button type="submit">Entrar</button>
    </form>
  </template>
  
  <script>
  import { mapMutations } from 'vuex';
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      ...mapMutations(['logar']),
      async login() {
        try {
          const response = await fetch('http://localhost:8000/token/', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              username: this.username,
              password: this.password
            })
          });
  
          if (response.ok) {
            const data = await response.json();
            this.logar(data.token);
            this.$setCookie('token',data.token);
            this.$router.push('/');
          } else {
            console.error('Erro ao fazer login');
          }
        } catch (error) {
          console.error(error);
        }
      },
    }
  };
  </script>
  