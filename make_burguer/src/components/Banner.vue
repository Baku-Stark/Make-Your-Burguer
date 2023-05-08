<template>
    <div class="main-banner">
        <h1>Make Your Burger</h1>
    </div>
</template>

<style scoped lang="scss">
    @import '@/assets/sass/variables';
    div.main-banner{
        height: 500px;
        background-position: 0 -250px;
        background-size: cover;
        background-repeat: no-repeat;
        background-image: url('@/../public/assets/img/burger.jpg');
        @include FlexBox-Pattern(center, flex-start);

        @include screenTablet{
            background-position: 0;
        }

        h1{
            font-size: 60px;
            padding: 20px 40px;
            text-align: center;
            color: #FCBA03;
            background-color: #222;
        }
    }
</style>
  
<script lang="ts">
export default{
    name: 'Banner',
};
</script>
  