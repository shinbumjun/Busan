<template>
  <div id="app">
    <nav_bar></nav_bar>
    <router-view v-bind:propsdata="userList"></router-view>    
    <Main_footer></Main_footer>
  </div>
</template>

<script>
import axios from 'axios';
import footer from './components/include/footer.vue'
import nav_bar from './components/include/nav_bar.vue'

let url = "http://127.0.0.1:8000/";  // 장고 drf 서버 주소

export default {
  name: 'App',
  components: {
    'Main_footer': footer,
    'nav_bar': nav_bar
  },
  data:() =>{
    return{
      userList:[]
    };
  },
  mounted(){
    axios({
      method:"GET",
      url:url
    })
    .then(response => {
      this.userList = response.data;
    })
    .catch(response => {
      console.log("Failed", response);
    });
  },
  methods:{ //CRUD Logic
    getUserList: function(){

    },
    updateUserList:function(){

    },
    deleteUserList:function(){

    }
  }
}
</script>

<style>

</style>
