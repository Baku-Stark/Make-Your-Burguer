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

<style lang="scss">
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Poppins', sans-serif;
  }

  div.main-container{
    margin: 50px;
    min-height: 250px;

    h2{
      font-size: 42px;
      margin-bottom: 30px;
      text-align: center;
      color: #222;
    }
  }
</style>
