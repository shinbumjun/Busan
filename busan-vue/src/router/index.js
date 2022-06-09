import Vue from 'vue';
import VueRouter from 'vue-router';
import example1 from '../components/ex-ex1.vue';
import example2 from '../components/ex-ex2.vue';
import example3 from '../components/ex-ex3.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/ex1',
            component: example1
        },
        {
            path: '/ex2',
            component: example2
        },
        {
            path: '/ex3',
            component: example3
        },
    ]   
})