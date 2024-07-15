import { createApp } from 'vue'

//Router
import router from './router'
//Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
const vuetify = createVuetify({components, directives})

//Components
import App from './App.vue'


createApp(App).use(router).use(vuetify).mount('#app')
