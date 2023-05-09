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
                        <option
                            v-for="pao in paes"
                            :key="pao.id"
                            :value="pao.tipo"
                        >
                            {{ pao.tipo }}
                        </option>
                    </select>
                </div>
                <div class="input-container">
                    <label for="carne">Escolha a carne do seu burger:</label>
                    <select
                        name="carne"
                        id="carne"
                        v-model="carne"
                    >
                        <option
                            v-for="carne in carnes"
                            :key="carne.id"
                            :value="carne.tipo"
                        >
                            {{ carne.tipo }}
                        </option>
                    </select>
                </div>
                <div id="opc-container" class="input-container">
                    <label id="opc-title">Escolha os opcionais:</label>
                    <div
                        class="checkbox-container"
                        v-for="opcional in opcionaisdata"
                        :key="opcional.id"
                    >
                        <input
                            type="checkbox" 
                            name="opcionais"
                            v-model="opcional.tipo" 
                            :value="opcional.tipo"
                        >
                        <span>
                            {{ opcional.tipo }}
                        </span>
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
            status: "Requested",
            msg: null,
        }
      },

      methods:{
        async getIngredientes(){
            /*
                PEGAR OS INGREDIENTES DA API
            */

            const req = await fetch("http://localhost:5000/ingredientes")

            if(req.status == 200){
                const data = await req.json()

                console.log(data)
                
                // CONVERTENDO PROXY PARA OBJECT
                this.paes = JSON.parse(JSON.stringify(data.data.ingredientes.paes))

                this.carnes = JSON.parse(JSON.stringify(data.data.ingredientes.carnes))

                this.opcionaisdata = JSON.parse(JSON.stringify(data.data.ingredientes.opcionais))
            }
        }
      },

      mounted(){
        this.getIngredientes()
      }
    });
  </script>  