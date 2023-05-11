<template>
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-12 top-footer">
                    <h4>
                        Make Your Burguer &copy; 2023
                    </h4>
                </div>
                <div class="col-12 top-footer">
                    <img class="vue-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original-wordmark.svg" />
                </div>
                <hr class="mt-5 mb-5">
                <div class="col-12 mid-footer">

                    <div class="column-contacts">
                        <div class="contacts-header">
                            <h4>Contatos</h4>
                        </div>
                        <div class="contacts-body">
                            <article>
                                <a href="http://wallacefmds360@outlook.com/" target="_blank">
                                    <img src="https://img.shields.io/badge/Outlook-1DA1F2?style=for-the-badge&logo=microsoft&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                            <article>
                                <a href="https://tamakiamajiki360@gmail.com/" target="_blank">
                                    <img src="https://img.shields.io/badge/GMAIL-1DA1F2?style=for-the-badge&logo=gmail&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                        </div>
                    </div>
                    <div class="column-contacts">
                        <div class="contacts-header">
                            <h4>Redes Sociais</h4>
                        </div>
                        <div class="contacts-body">
                            <article>
                                <a href="https://twitter.com/Walleemc2" target="_blank">
                                    <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                            <article>
                                <a href="https://www.linkedin.com/in/wallace-freitas-92a2061b6/" target="_blank">
                                    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                            <article>
                                <a href="https://instagram.com/wallace_emc2" target="_blank">
                                    <img src="https://img.shields.io/badge/-Instagram-6610F2?style=for-the-badge&logo=Instagram&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                            <article>
                                <a href="https://www.reddit.com/user/StarkBakuha" target="_blank">
                                    <img src="https://img.shields.io/badge/Reddit-FF4500?style=for-the-badge&logo=reddit&logoColor=111111&color=F0F8FF" height="30" width="100"/>
                                </a>
                            </article>
                        </div>
                    </div>
                    <div class="column-contacts">
                        <div class="contacts-header">
                            <h4>Outros Projetos</h4>
                        </div>
                        <div class="contacts-body">
                            <article>
                                <a href="https://baku-stark.github.io/Portfolio-Wallace/indexBaku.html" target="_blank">
                                    <img src="https://img.shields.io/badge/Portfolio-%23000000.svg?style=for-the-badge&logo=firefox&logoColor=#FF7139&"
                                    height="30" width="200"/>
                                </a>
                            </article>
                            <article>
                                <a href="https://discord.com/api/oauth2/authorize?client_id=1055540316725313626&permissions=8&scope=applications.commands%20bot" target="_blank">
                                    <img src="https://img.shields.io/badge/BOT Spright Blue-%23000000.svg?style=for-the-badge&logo=discord&logoColor=#FF7139&"
                                    height="30" width="200"/>
                                </a>
                            </article>
                        </div>
                    </div>

                </div>
                <hr class="mt-5 mb-5">
                <div class="col-12 bot-footer">
                    <p>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Iure ullam, minima perspiciatis voluptas sit quae eos nisi blanditiis excepturi tenetur doloremque impedit exercitationem dolore voluptates aspernatur, dolores minus, iste adipisci.
                    </p>
                </div>
            </div>
        </div>
    </footer>
</template>

<style scoped lang="scss">
    @import '@/assets/sass/variables';
    footer{
        width: 100%;
        padding: 20px;
        background-color: #f0f8ff;

        div.top-footer{
            text-align: center;

            img.vue-icon{
                width: 100px;
                height: 100px;
            }
        }

        div.mid-footer{
            gap: 20px;
            @include GridLayout-Columns(repeat(3, 1fr));

            div.column-contacts{
                div.contacts-header{
                    text-align: center;
                    h4{
                        font-size: 2rem;
                        font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
                    }
                }

                div.contacts-body {
                    text-align: center;

                    article{
                        margin-bottom: 1vh;
                    }
                }
            }

            @include screenTablet{
                place-items: center;
                @include GridLayout-Columns(repeat(1, 1fr));

                div.column-contacts{
                    width: 50vw;
                }
            }
        }

        div.bot-footer{
            text-align: center;

            p{
                opacity: .7;
                font-style: italic;

                a{
                    text-decoration: none;
                    color: #212529;

                    &:hover{
                        text-decoration: underline;
                    }
                }
            }
        }

        hr{
            background-color: #616060;
        }
    }
</style>

<script lang="ts">
export default {
    name: "Footer"
}
</script>