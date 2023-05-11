<template>
  <div class="main-container">
    <h2>Pedidos</h2>
    <div class="cards-grid">
      <div
          v-for="req of request"
          :key="req.id"
        >
          <div class="card-body-request">
            {{ req.nome }}
          </div>
        </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
  @import '../assets/sass/variables';

  div.cards-grid{
    @include GridLayout-Columns(repeat(4, 1fr));

    @include screenTablet{
      @include GridLayout-Columns(repeat(2, 1fr));
    }

    @include screenPhone{
      @include GridLayout-Columns(repeat(1, 1fr));
    }

    div.card-body-request{
      margin: 5px;
      border-radius: 15px;
      background-color: #111111;
    }
  }
</style>

<script lang="ts">
  import { defineComponent } from "vue";
  export default defineComponent({
    name: 'Pedidos',

    data(){
      return{
        request: []
      }
    },

    methods:{
      changeTitle(){
        /*
            ALTERAR O TÍTULO DA PÁGINA
        */
          
        document.title = "Faça seu pedido"
      },
      async getPedidos(){
        /*
              PEGAR OS PEDIDOS DA API
        */
        this.changeTitle()
        const req = await fetch("http://localhost:5000/api/ingredientes")

        if(req.status == 200){
          const data = await req.json()

          const statusCDN = '[ API-FLASK/PEDIDOS ]'
          const message = '200 - OK'
          console.log(
            `%c ${statusCDN} %c ${message} `, 
            'background: #69ACEB; color: #f0eff5; font-weight: bold;',
            'background: #f0f8ff; color: #111111; font-weight: bold;'
          );

          console.log(data.data.burgers)

          for(const request of data.data.burgers){
            console.log(request)
          }
                
          // CONVERTENDO PROXY PARA OBJECT
          this.request = JSON.parse(JSON.stringify(data.data.burgers))

          console.log(this.request)
        }
      }
    },

    mounted(){
      this.getPedidos()
    }
  });
</script>

