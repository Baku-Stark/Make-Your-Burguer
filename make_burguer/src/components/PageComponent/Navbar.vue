<template>
    <nav>
        <router-link to="/">
            <img
                id="logo"
                :src="src"
                :alt="alt"
            >
        </router-link>

        <router-link
        to="/about"
        title="Sobre o Projeto"
        >
            About
        </router-link>
    </nav>
</template>

<style scoped lang="scss">

</style>

<script lang="ts">
export default {
    name: "Navbar",
    props:[
        "src","alt"
    ]
}
</script>