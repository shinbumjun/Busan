import Vue from 'vue'
import App from './App.vue'
import router from './router/index.js';
import axios from 'axios'
import { store } from './store/store';

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

axios.defaults.baseURL = 'http://127.0.0.1:8000/'

