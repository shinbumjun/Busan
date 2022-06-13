import Vue from 'vue';
import VueRouter from 'vue-router';
import BusanCommunity from '../components/BusanCommunity.vue';
import BusanCommunityinsertform from '../components/BusanCommunityinsertform.vue';
import BusanCommunitydetail from '../components/BusanCommunitydetail.vue';
import BusanFavorites from '../components/BusanFavorites.vue';
import BusanTouristspotdetails from '../components/BusanTouristspotdetails.vue';
import BusanTouristspot from '../components/BusanTouristspot.vue';
import BusanCourse from '../components/BusanCourse.vue';
import BusanHome from '../components/BusanHome.vue';
import BusanLog_in from '../components/BusanLog_in.vue';
import BusanMypage from '../components/BusanMypage.vue';
import BusanRecommand_result from '../components/BusanRecommand_result.vue';
import BusanRecommand_select from '../components/BusanRecommand_select.vue';
import BusanSign_up from '../components/BusanSign_up.vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode: 'history',
    scrollBehavior() { 
        return { x: 0, y: 0 } 
    },
    routes: [
        {
            path: '/',
            component: BusanHome
        },
        {
            path: '/login',
            component: BusanLog_in
        },
        {
            path: '/signup',
            component: BusanSign_up
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
            path: '/community',
            component: BusanCommunity
        },
        {
            path: '/communityinsertform/',
            component: BusanCommunityinsertform
        },
        {
            path: '/communitydetail/:id',
            component: BusanCommunitydetail
        },
        {
            path: '/favorites',
            component: BusanFavorites
        },
        {
            path: '/touristspotdetails/:id',
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