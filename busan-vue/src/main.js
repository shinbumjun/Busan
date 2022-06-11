import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js';
import axios from 'axios'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

axios.defaults.baseURL = 'https://apidjackets.codewithstein.com'


// createApp(App).use(store).use(router, axios).mount('#app')
