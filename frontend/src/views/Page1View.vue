<template>
    <div>
      <h3>Pagina 1</h3>
      <p>essa pagina precisa de login</p>
      <b-table striped hover :items="items"></b-table>
    </div>
</template>

<script>
export default {
  data(){
    return {
      items:[
        {'idade':32,'nome': 'carlos','sobrenome':'agnes'},
        {'idade':54,'nome': 'joão','sobrenome':'carlos'},
        {'idade':22,'nome': 'joaquins','sobrenome':'freitas'}
      ]
    }
  }
}
</script>
  
 