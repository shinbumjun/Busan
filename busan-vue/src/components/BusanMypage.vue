<template>
    <div>
        <!-- Head IMG Part -->
        <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="../../public/Headbar_Busan_3.png" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>마이페이지</p>
                            <p style="font-size: 30px;">Mypage</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Content Part-->
        <div class="container" style="height:1000px">
            <form  id="myForm">
                <div>
                    <label class="control-label" for="users_id">아이디</label>
                    <input v-model="user_id" class="form-control" type="text" name="users_id" id="users_id" value="{}"  placeholder=""  style="outline: 0;"/>
                    <div id="id_length_validation" class="invalid-feedback">영문자 소문자로 시작하고 5~10글자 이내로 작성해주세요.</div>
                    <div id="id_overlap_validation" class="invalid-feedback">중복된 아이디 입니다.</div>
                </div>		
                <div>
                    <label class="control-label" for="users_name">이름</label>
                    <input v-model="name" class="form-control" type="text" name="users_name" id="users_name" value="{}"/>
                </div>
                <div>
                    <label class="control-label" for="users_pwd">비밀번호</label>
                    <input class="form-control" type="password" name="users_pwd" id="users_pwd" disabled/>
                    <div id="pwd_length_validation" class="invalid-feedback">영문자,숫자,특수문자를 하나이상을 사용해주세요.</div>
                    <div id="pwd_length_validation" class="valid-feedback">비밀번호 확인</div>
                </div>
                <div>
                    <label class="control-label" for="users_email">이메일</label>
                    <input v-model="email" class="form-control" type="text" name="users_email" id="users_email" value="{}"/>
                    <div class="invalid-feedback">이메일 형식을 확인 하세요.</div>
                </div>
                <div style="margin-top:50px; padding-top:40px;">
                    <button @click="userUpdate" class="btn btn-primary submit-btn" type="submit" style="border:none; width: 350px;">수정하기</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from "axios";
let url = "http://127.0.0.1:8000/auth/user/";

export default {
    props:["propsdata"],
    data(){
        return{
                user_id:"",
                name:"",
                email:""
        }
    },
    created(){
        this.user_id = this.propsdata.user.user_id,
        this.name = this.propsdata.user.name,
        this.email= this.propsdata.user.email
    },
    mounted(){  
    },
    methods:{
        userUpdate() {
            let saveData = {};
            saveData.user_id = this.data.user_id;
            saveData.name = this.data.name;
            saveData.email = this.data.email;

                axios({
                method:"PUT",
                url:url,
                data: this.data
                })
                .then((res) => {
                    if (res.status === 200) {
                    // 로그인 성공시 처리해줘야할 부분
                            console.log("",res.data)
                            this.$emit("saved",this.data)
                            this.$router.push("/")
                    }
                    
                })
                .catch(error => {
                    console.log("Failed to update",error.response);
                });
            },
    }
} 
</script>

<style>
        /* Head IMG CSS*/
        .head img{
            height: 450px;
            filter: brightness(90%);
        }
        .subject{
            vertical-align: middle;
            display:inline-block;  
            width:250px; 
            border-color: rgba(0, 0, 0, 0.5);
            text-align:left; 
            height: 350px;
            font-family: 'Gugi', cursive;
            font-size: 50px;
            color:white;
            margin-left: 20%;
            position: absolute;
            left: 0;
            bottom: 0;
        }
        .subject p:first-child{
            margin-bottom: 0px;
        }    
        /* Content CSS*/
        .container{
            font-family: 'Noto Sans KR', sans-serif;
            color:#42464A;
        }
        .head1{
            margin: 80px 100px;
            text-align: center;
            display:flex;
            flex-direction: column;
            align-items: center;
            font-size: 30px;
            font-weight: bold;
            padding-bottom:70px;
            border-bottom:1px solid;
        }
        #myForm{
            display:flex;
            flex-direction:column;
            margin: 0px 100px;
        }
        #myForm label{
            margin-top:60px;
            text-align:center;
            display:inline-block;
            width:120px;
            height:30px;
            vertical-align:center;
            font-weight:bold;
        }
        #myForm input{
            border:none;
            padding:7px 5px;
            font-size: 17px;
            margin-top: 5px;
            border-bottom:1.5px solid rgba(29,63,109,0.4);
            transition: border-color 0.6s ease-in-out;
            display:inline-block;
            width : 500px;
        }
        #myForm div{
            text-align: center;
        }
        #myForm input:focus, #myForm input:hover{
            border-color: rgb(111, 0, 255);
        }
        #myForm input:focus{
            outline: 0;
        }
        .submit-btn{
            background-color: #007cc4;
        }
        .submit-btn:hover{
            background-color:rgb(111, 0, 255) ;
        }
        #myForm button{
            margin-top: 17px;
            margin-bottom: 30px;
            padding: 13px;
            font-weight: bold;
            font-size: 15px;
            opacity: 0.7;
            color:rgba(255,255,255,0.9);
            border-radius: 8px;
            cursor: pointer;
            width : 200px;
            display:inline-block;
        }
</style>