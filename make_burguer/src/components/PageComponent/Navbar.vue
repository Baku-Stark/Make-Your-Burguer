<template>
    <nav>
        <router-link to="/" id="logo_url">
            <img
                id="logo"
                :src="src"
                :alt="alt"
            >
        </router-link>

        <router-link
            to="/"
            title="Página principal"
        >
            Home
        </router-link>

        <router-link
            to="/pedidos"
            title="Sobre o Projeto"
        >
            Pedidos
        </router-link>
    </nav>
</template>

<style scoped lang="scss">
    @import '@/assets/sass/variables';
    nav{
        padding: 15px 50px;
        background-color: #222;
        border-bottom: 4px solid #111;
        @include FlexBox-Pattern(center, flex-end);

        a{
            margin: 12px;
            transition: .5s;
            text-decoration: none;
            color: #FCBA03;

            &:hover{
                color: #FFF;
            }
        }

        #logo_url{
            margin: auto;
            margin-left: 0;

            img#logo{
                width: 40px;
                height: 40px;
            }
        }
    }
</style>

<script lang="ts">
export default {
    name: "Navbar",
    props:[
        "src","alt"
    ]
}
</script>