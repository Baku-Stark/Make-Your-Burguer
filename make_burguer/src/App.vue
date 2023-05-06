<template>
  <Navbar
    :src="logo_src"
    :alt="logo_alt"
  />
  <router-view/>
  <Footer/>
</template>

<script lang="ts">
  import Navbar from './components/PageComponent/Navbar.vue'
  import Footer from './components/PageComponent/Footer.vue';

  export default {
    components:{
      Navbar,
      Footer
    },
    data(){
      return{
        logo_src: "assets/img/logo.png",
        logo_alt: "Make Your Burguer"
      }
    }
  }
</script>

<style>
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }
</style>
