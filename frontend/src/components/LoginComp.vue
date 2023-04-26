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
  import { mapGetters } from 'vuex';
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    computed:{...mapGetters(['getDominio','getToken'])},
    methods: {
      ...mapMutations(['logar','setUser']),
      async login() {
        try {
          const response = await fetch(`${this.getDominio}/token/`, {
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
            this.userData()
          } else {
            console.error('Erro ao fazer login');
          }
        } catch (error) {
          console.error(error);
        }
      },
      async userData(){
        try{
        this.esperando = true
        const response = await fetch(`${this.getDominio}/token-user/`,{
          headers:{
            'Authorization': `Token ${this.getToken}`
          }
        });
        if(!response.ok){
          throw new Error('Failed to fetch data');
        }
        const data = await response.json()
        this.$setCookie('nome',data.username);
        this.setUser(data.username)
        this.$router.push('/');
      }catch(error){
        alert(error)
      }
      }
    }
  };
  </script>
  