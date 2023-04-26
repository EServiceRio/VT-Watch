<template>
   <div>
        
        <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand href="#">
          <img class="mr-3" src="../assets/logo novo.jpeg" width="120" height="40">
        </b-navbar-brand>
    
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    
        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item><router-link to="/">Home</router-link></b-nav-item>
            <b-nav-item><router-link to="/fabrica/">Fábrica</router-link></b-nav-item>
            <b-nav-item><router-link to="/user/profile">Usuario</router-link></b-nav-item>
          </b-navbar-nav>
         
          <b-navbar-nav class="ml-auto mr-2">
            <div class="m-auto">
              <img :src="dxm_online" width="30" height="30" />
            </div>
            <b-nav-item-dropdown right v-if="logado">
              <template #button-content>
                <em>
                  Olá {{getNome}}
                  <b-avatar badge-variant="danger" variant="primary"></b-avatar>
                </em>
              </template>
              <div>
                 <b-button @click="deslogar" variant="primary">sair</b-button>
              </div>
            </b-nav-item-dropdown>
            <div  class="m-auto" v-else>
              <b-nav-item><router-link to="/login/">Logar</router-link></b-nav-item>
            </div>
          </b-navbar-nav>
    
        </b-collapse>
      </b-navbar>
        
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { mapMutations } from 'vuex'
export default {
    name:'main_menu',
    created(){
      this.load()
      setInterval(()=>{this.load()},5000)
    },
    methods:{
      ...mapMutations(['logout','dxmSetOn','dxmSetOff']),
      load(){
        this.getDados()
      },
      deslogar(){
        this.logout()
        this.$apagaCookies()
        setTimeout(() => {
          this.$router.push('/');
        }, 2000);
      },
      async getDados() {
        try {
          const response = await fetch(`${this.getDominio}/api/dxm/`, {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Token ${this.getToken}`
            },
          });
  
          if (response.ok) {
            const data = await response.json();
            if(data.online){
              this.dxmSetOn()
             }else{
              this.dxmSetOff()
             }
          } else {
            console.error('Erro ao fazer login');
          }
        } catch (error) {
          console.error(error);
        }
      }
    },
    computed:{
      ...mapGetters(['logado','getNome','getInicial','dxmOnline','getDominio','getToken']),
      dxm_online(){
        if(this.dxmOnline){
          return this.$getImgUrl("notifiOk","png")
        }else{
          return this.$getImgUrl("notifiFalha","png")
        }
      }
    },
}
</script>