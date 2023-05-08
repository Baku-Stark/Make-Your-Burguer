<template>
  <Banner/>
  <div class="main-container">
    <h2>Monte o seu burguer</h2>
    <BurgerForm/>
  </div>
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import Banner from '@/components/Banner.vue';
    import BurgerForm from '@/components/BurgerForm.vue';
    
    export default defineComponent({
      name: 'HomeView',

      components:{
        Banner,
        BurgerForm
      },

      methods:{
        async changeTitle(){
          /*
              ALTERAR O TÍTULO DA PÁGINA
          */
          
          document.title = "Make Your Burger"
        }
      },

      mounted(){
        this.changeTitle()
        }
      });
</script>
