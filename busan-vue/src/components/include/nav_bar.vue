<template>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color:white; height: 60px;">
        <div class="container-fluid">
            
            <button class="navbar-brand BFU" href="#">
                <router-link to="/home">
                    <img src="../../../public/BusanForU Logo3.png">
                </router-link>
            </button>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse navMid" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0 navMid_ul">
                    <li class="nav-item">
                        <a class="nav-link"><router-link to="/recommand_select">추천</router-link></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"><router-link to="/course">코스</router-link></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"><router-link to="/touristspot">관광지</router-link></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link"><router-link to="/community">커뮤니티</router-link></a>
                    </li>
                </ul>
                <div class="navEnd">
                    <button class="Btn" v-if = "propsdata.user.user_id!=null">
                        <router-link to="/mypage">{{propsdata.user.user_id}}</router-link>
                    </button>
                    <button class="Btn" v-else>
                        <router-link to="/">로그인</router-link>
                    </button>
                    <span>|</span>
                    <button class="Btn" >
                        <router-link to="/favorites">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-star" viewBox="0 0 16 16">
                                <path d="M2.866 14.85c-.078.444.36.791.746.593l4.39-2.256 4.389 2.256c.386.198.824-.149.746-.592l-.83-4.73 3.522-3.356c.33-.314.16-.888-.282-.95l-4.898-.696L8.465.792a.513.513 0 0 0-.927 0L5.354 5.12l-4.898.696c-.441.062-.612.636-.283.95l3.523 3.356-.83 4.73zm4.905-2.767-3.686 1.894.694-3.957a.565.565 0 0 0-.163-.505L1.71 6.745l4.052-.576a.525.525 0 0 0 .393-.288L8 2.223l1.847 3.658a.525.525 0 0 0 .393.288l4.052.575-2.906 2.77a.565.565 0 0 0-.163.506l.694 3.957-3.686-1.894a.503.503 0 0 0-.461 0z"/>
                            </svg>
                        </router-link>
                    </button>
                </div>
            </div>
        </div>
    </nav>
</template>

<script>
export default{
    name: 'nav_bar',
    props: ["propsdata"],
    mounted(){
        
    }
}
</script>

<style>
    .navbar{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 100;
        }
        .BFU{
            font-family: 'Lobster', cursive;
            border: 0;
            outline: 0;
            background-color: white;
            width:210px;
            margin-left: 80px;
        }
        .BFU p{
            display:inline-block;
        }
        .BFU img{
            width: 200px;
            height: 80px;
            margin-top: 30px;
        }
        .navMid{
            font-family: 'IBM Plex Sans KR', sans-serif;
            font-size: 18px;
            font-weight: bold;
        }
        .navMid_ul {
            margin-left: auto;
            margin-right: auto;
        }
        .navMid_ul li{
            display: inline-block;
            width: 90px;
        }
        .Btn{
            border: 0;
            outline: 0;
            background-color: white;   
            margin-right: 10px; 
            margin-left: 10px;
        }
        .navEnd{
            margin-right: 80px;
        }
        .navEnd button{
            font-weight: bold;
            font-family: 'IBM Plex Sans KR', sans-serif;
        }
        .navEnd span{
            color:rgb(83, 46, 0)
        }

</style>