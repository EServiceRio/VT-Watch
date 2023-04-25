<template>
    <div>
        <h1>login de Usuario</h1>
        <div class="m-auto p-5" style="max-width: 400px">   
            <Login dominio="http://localhost:8000" @logou="alert('foi')"></Login>
        </div>
    </div>
</template>

<script>
import Login from '@/components/LoginComp.vue'
export default {
    components:{
        Login
    }
}
</script>