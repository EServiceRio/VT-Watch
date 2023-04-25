import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
      logado: false,
      nome: 'Desconhecido',
      token: '',
      avatar: '',
  },
  getters: {	  
    logado(state){
      return state.logado
    }
  },
  mutations: {	
    logar(state,token){
      state.logado = true
      state.token = token
    },
    logout(state){
      state.logado = false
      state.token = ''
    }
  },
  actions: {
  },
  modules: {
  }
})
