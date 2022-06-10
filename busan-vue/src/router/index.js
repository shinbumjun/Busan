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
import BusanHome from '../components/BusanHome.vue';
import BusanLog_in from '../components/BusanLog_in.vue';
import BusanMypage from '../components/BusanMypage.vue';
import BusanRecommand_result from '../components/BusanRecommand_result.vue';
import BusanRecommand_select from '../components/BusanRecommand_select.vue';
import BusanSign_up from '../components/BusanSign_up.vue';
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
            path: '/',
            component: BusanHome
        },
        {
            path: '/login',
            component: BusanLog_in
        },
        {
            path: '/mypage',
            component: BusanMypage
        },
        {
            path: '/recommand_result',
            component: BusanRecommand_result
        },
        {
            path: '/recommand_select',
            component: BusanRecommand_select
        },
        {
            path: '/signup',
            component: BusanSign_up
        },
    ]   
})