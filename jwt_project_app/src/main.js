import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import VueCollapsiblePanel from '@dafcoe/vue-collapsible-panel'

axios.defaults.baseURL = 'http://localhost:8000'


createApp(App).use(store).use(router, axios).use(VueCollapsiblePanel).mount('#app')
