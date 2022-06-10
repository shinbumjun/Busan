import Vue from 'vue';
import VueRouter from 'vue-router';
import example1 from '../components/ex-ex1.vue';
import example2 from '../components/ex-ex2.vue';
import example3 from '../components/ex-ex3.vue';
import BusanCommunity from '../components/BusanCommunity.vue';
import BusanCommunityinsertform from '../components/BusanCommunityinsertform.vue';
import BusanCommunitydetail from '../components/BusanCommunitydetail.vue';
import BusanFavorites from '../components/BusanFavorites.vue';
import BusanTouristspotdetails from '../components/BusanTouristspotdetails.vue';
import BusanTouristspot from '../components/BusanTouristspot.vue';
import BusanCourse from '../components/BusanCourse.vue';

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
        {
            path: '/community',
            component: BusanCommunity
        },
        {
            path: '/communityinsertform',
            component: BusanCommunityinsertform
        },
        {
            path: '/communitydetail',
            component: BusanCommunitydetail
        },
        {
            path: '/favorites',
            component: BusanFavorites
        },
        {
            path: '/touristspotdetails',
            component: BusanTouristspotdetails
        },
        {
            path: '/touristspot',
            component: BusanTouristspot
        },
        {
            path: '/course',
            component: BusanCourse
        },
    ]   
})