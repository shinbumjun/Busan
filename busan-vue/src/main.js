import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js';

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')


/*
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

axios.defaults.baseURL = 'https://apidjackets.codewithstein.com'

createApp(App).use(store).use(router, axios).mount('#app')
*/