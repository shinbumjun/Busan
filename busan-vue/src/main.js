import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js';

import axios from 'axios';


Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

