<template>
  <div id="app">
    <nav_bar v-bind:propsdata="userList"></nav_bar>
    <router-view v-bind:propsdata="userList" v-on:saved="getUserList"></router-view>    
    <!-- v-bind:하위컴포넌트 속성명="상위 컴포넌트 전달할 데이터명"  -->
    <Main_footer></Main_footer>
  </div>
</template>

<script>
import axios from 'axios';
import footer from './components/include/footer.vue';
import nav_bar from './components/include/nav_bar.vue';

let url = "http://127.0.0.1:8000/";  // 장고 drf 서버 주소

export default {
  name: 'App',
  components: {
    'Main_footer': footer,
    'nav_bar': nav_bar,
  },
  data:() =>{
    return{
      userList:[],
      userSelect:[],
      user:{
        user_id : "",
        password : ""
      }
    };
  },
  mounted(){
     // DOM 객체 생성 후 DRF 서버에서 데이터를 가져와 userList에 저장
    
    axios({
      method:"POST",
      url:url+"auth/login/",
      data:this.user
    })
    .then(response => {
      this.userList = response.data;
      console.log("Success",response);
    })
    .catch(error => {
      console.log("Failed to get userList",error.response);
    });
    
  },
  methods:{ //CRUD Logic
     getUserList: function(data) {
        this.user.user_id = data.user_id,
        this.user.password = data.password
          axios({
            method: "POST",
            url: url+"auth/login/",
            data:this.user
          })
            .then(response => {
              this.userList = response.data;
              console.log("Success", response);
            })
            .catch(error => {
              console.log("Failed to get userList", error.response);
            });
    },
    getSelectList: function() {
      axios({
        method: "GET",
        url: url+"/"
      })
        .then(response => {
          this.userSelect = response.data;
          console.log("Success", response);
        })
        .catch(error => {
          console.log("Failed to get userSelect", error.response);
        });
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
