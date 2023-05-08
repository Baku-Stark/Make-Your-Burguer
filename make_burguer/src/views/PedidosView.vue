<template>
  <div class="main-container">
    <h2>Pedidos</h2>
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  export default defineComponent({
    name: 'Pedidos',

    methods:{
        async changeTitle(){
          /*
              ALTERAR O TÍTULO DA PÁGINA
          */
          
          document.title = "Faça seu pedido"
        }
      },

      mounted(){
        this.changeTitle()
      }
  });
</script>

