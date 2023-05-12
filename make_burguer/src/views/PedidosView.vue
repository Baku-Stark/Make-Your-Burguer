<template>
  <div class="main-container">
    <h2>Pedidos</h2>
    <div class="cards-grid">
      <div
          v-for="req of request"
          :key="req.id"
        >
          <div class="card-body-request">
            <div class="card-header-request">
              <h4>{{ req.nome }}</h4>
            </div>
            <div class="card-section-request">
                <ul>
                  <li>{{ req.pao }}</li>
                  <li>{{ req.carne }}</li>
                  <li>
                    <details>
                      <summary>Opcionais</summary>
                      <p
                        v-for="opc of req.opcionais"
                        :key="opc"
                      >
                        {{ opc }}
                      </p>
                    </details>
                  </li>
                </ul>
            </div>
            <div class="card-footer-request">
                <p>
                  Status: <span>{{ req.status }}</span>
                </p>
            </div>
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
      @include GridLayout-Columns(repeat(1, 1fr));

      div.card-header-request, 
      div.card-section-request,
      div.card-footer-request{
        padding: 10px;
      }

      div.card-header-request{
        text-align: center;

        h4{
          color: #FCB403;
        }
      }

      div.card-section-request{
        ul{
          list-style: none;

          li{
            color: #fac235;

            details summary{
              font-weight: bold;
            }

            details p{
              color: #fff3d5;
              margin-bottom: 0 !important;
              margin-left: 5vw;
            }
          }
        }
      }

      div.card-footer-request{
        p{
          color: #f0f8ff;
          font-weight: bold;
          text-align: center;

          span{
            color: #FCB403;
          }
        }
      }
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
                
          // CONVERTENDO PROXY PARA OBJECT
          this.request = JSON.parse(JSON.stringify(data.data.burgers))
        }
      }
    },

    mounted(){
      this.getPedidos()
    }
  });
</script>

