<template>
  <Banner/>
  <div class="main-container">
    <h2>Monte o seu burguer</h2>
    <BurgerForm/>
  </div>
</template>

<script lang="ts">
  import Banner from '@/components/Banner.vue';
  import BurgerForm from '@/components/BurgerForm.vue';

  document.title = "Make Your Burger"

  export default{
    name: 'HomeView',
    components:{
      Banner,
      BurgerForm
    },
  };
</script>
