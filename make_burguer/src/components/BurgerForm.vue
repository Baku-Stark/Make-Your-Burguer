<template>
    <div>
        <p>Componente de Mensagem</p>
        <div>
            <form method="post">
                <div class="input-container">
                    <label for="nome">Nome do cliente:</label>
                    <input
                        type="text"
                        name="name"
                        id="nome"
                        v-model="nome" 
                        placeholder="Digite o seu nome"
                    >
                </div>
                <div class="input-container">
                    <label for="pao">Escolha o pão:</label>
                    <select
                        name="pao"
                        id="pao"
                        v-model="pao"
                    >
                        <option value="">Selecione o seu pão</option>
                        <option value="integral">Integral</option>
                    </select>
                </div>
                <div class="input-container">
                    <label for="carne">Escolha a carne do seu burger:</label>
                    <select
                        name="carne"
                        id="carne"
                        v-model="carne"
                    >
                        <option value="">Selecione a sua carne</option>
                        <option value="1">Picanha</option>
                    </select>
                </div>
                <div id="opc-container" class="input-container">
                    <label id="opc-title">Escolha os opcionais:</label>
                    <div class="checkbox-container">
                        <input
                            type="checkbox" 
                            name="opcionais"
                            v-model="opcionais" 
                            value="salame"
                        >
                        <span>Salame</span>
                    </div>
                </div>
                <div class="input-container">
                    <input type="submit" value="Criar meu Burger">
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped lang="scss">
    form{
        margin: 0 auto;
        max-width: 400px;

        div.input-container{
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;

            label{
                padding: 5px 10px;
                margin-bottom: 15px;
                font-weight: bold;
                color: #222;
                border-left: 4px solid #FCB403;
            }

            input, select{
                width: 300px;
                padding: 5px 10px;
            }

            label#opc-title{
                width: 100%;
            }

            input[type="submit"]{
                padding: 10px;
                transition: .5s;
                margin: 0 auto;
                font-weight: bold;
                color: #FCB403;
                background-color: #222;
                border: 2px solid #222;

                &:hover{
                    cursor: pointer;
                    background-color: #fff;
                    border: 2px solid #FCB403;
                }
            }

            div.checkbox-container{
                width: 50%;
                margin-bottom: 20px;
                display: flex;
                align-items: flex-start;

                span{
                    margin-left: 6px;
                    font-weight: bold;
                }

                input[type="checkbox"], span{
                    width: auto;
                }
            }
        }

        div#opc-container{
            flex-wrap: wrap;
            flex-direction: row;
        }
    }
</style>
  
<script lang="ts">
    import { defineComponent } from "vue";
    
    export default defineComponent({
      name: 'BurgerForm',

      data(){
        return{
            paes: null,
            carnes: null,
            opcionaisdata: null,
            nome: null,
            pao: null,
            carne: null,
            opcionais : [],
            status: "Solicitado",
            msg: null,
        }
      },

      methods:{
        async getIngredientes(){
            /*
                PEGAR OS INGREDIENTES DA API
            */
            const req = await fetch("http://127.0.0.1:8000/ingredientes")
            const data = req.json()
            console.log(data)
        }
      },

      mounted(){
        this.getIngredientes()
      }
    });
  </script>  