<template>
    <div>
        <!-- Head IMG Part -->
        <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="../../public/Headbar_Busan_4.png" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>추천선택</p>
                            <p style="font-size: 30px;">Recommand Select</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Content Part-->
        <div class="box">
            <div class="content-top">
                <h1>어떤 여행을 원하시나요?</h1>
            </div>
            <div class="gender">
                <div>
                    <div class="label1">
                        <p>당신의 성별은 무엇인가요?</p>
                    </div>
                </div>
                <div style="text-align: center">
                    <input type="checkbox" id="man_check">
                    <label for="man_check"></label>
                    <input type="checkbox" id="woman_check">
                    <label for="woman_check"></label>
                </div>
                <div class="label1_explain" style=" text-align: center;">
                    <div>
                        <p>남성</p>
                    </div>
                    <div>
                        <p>여성</p> 
                    </div>
                </div>
            </div>
            <div class="age">
                <div>
                    <div class="label2">
                        <p>연령대가 어떻게 되시나요?</p>
                    </div>
                </div>
                <div style="text-align: center">
                    <input type="checkbox" id="check_10th">
                    <label for="check_10th"></label>
                    <input type="checkbox" id="check_20th">
                    <label for="check_20th"></label>
                    <input type="checkbox" id="check_30th">
                    <label for="check_30th"></label>
                    <input type="checkbox" id="check_40th">
                    <label for="check_40th"></label>
                    <input type="checkbox" id="check_50th">
                    <label for="check_50th"></label>
                </div>
                <div class="label2_explain" style=" text-align: center;">
                    <div>
                        <p>10대</p>
                    </div>
                    <div>
                        <p>20대</p> 
                    </div>
                    <div>
                        <p>30대</p> 
                    </div>
                    <div>
                        <p>40대</p> 
                    </div>
                    <div>
                        <p>50대 이상</p> 
                    </div>
                </div>
            </div>
            <div class="with">
                <div>
                    <div class="label3">
                        <p>누구와 함께 하시나요?</p>
                    </div>
                </div>
                <div style="text-align: center">
                    <input type="checkbox" id="check_solo">
                    <label for="check_solo"></label>
                    <input type="checkbox" id="check_couple">
                    <label for="check_couple"></label>
                    <input type="checkbox" id="check_friends">
                    <label for="check_friends"></label>
                    <input type="checkbox" id="check_family">
                    <label for="check_family"></label>
                </div>
                <div class="label3_explain" style=" text-align: center;">
                    <div>
                        <p>혼자</p>
                    </div>
                    <div>
                        <p>연인</p> 
                    </div>
                    <div>
                        <p>친구</p> 
                    </div>
                    <div>
                        <p>가족</p> 
                    </div>
                </div>
            </div>
            <div class="theme">
                <div class="theme_message">
                    <h1>원하시는 여행 테마를 선택하세요</h1>
                </div>
                <div>
                    <div class="theme_images" style="text-align: center;">
                        <div>
                            <input type="checkbox" id="check_nature">
                            <label for="check_nature"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_park">
                            <label for="check_park"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_culture">
                            <label for="check_culture"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_shopping">
                            <label for="check_shopping"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_interesting">
                            <label for="check_interesting"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_history">
                            <label for="check_history"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_walking">
                            <label for="check_walking"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_experience">
                            <label for="check_experience"></label>
                        </div>
                        <div>
                            <input type="checkbox" id="check_festival">
                            <label for="check_festival"></label>
                        </div>
                    </div>
                    <div class="theme_explain" style="text-align: center;">
                        <div>
                            <h1># 자연</h1>
                        </div>
                        <div>
                            <h1># 공원</h1>
                        </div>
                        <div>
                            <h1># 문화</h1>
                        </div>
                        <div>
                            <h1># 쇼핑</h1>
                        </div>
                        <div>
                            <h1># 이색 여행</h1>
                        </div>
                        <div>
                            <h1># 역사</h1>
                        </div>
                        <div>
                            <h1># 걷기</h1>
                        </div>
                        <div>
                            <h1># 체험</h1>
                        </div>
                        <div>
                            <h1># 축제</h1>
                        </div>
                    </div>
                    <div style="text-align: center; margin-top: 70px;">
                        <input class="submit" type="submit" value="추천받으러 Go!" style="margin-top:40px;"/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

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
        /* content Part */ 
        .box{
            margin-left: 0px;
            margin-right: 0px;
            height: 2650px;
            overflow: hidden;
        }
        .content-top{
            display: block;
            margin-top: 60px;
            margin-bottom: 60px;
        }
        .content-top h1{
            text-align: center;
            font-size: 40px;
            font-family: 'Do Hyeon', sans-serif;
        }
        .gender{
            position: relative;
            background-color: #F3FACF;
            height: 440px;
        }
        .label1{
            vertical-align: middle;
            display:inline-block; 
            background-color: rgba(255, 171, 45, 0.753); 
            width:300px; 
            color: white;
            text-align:center; 
            height: 60px;
            line-height: 60px;
            font-family: 'Gugi', cursive;
            font-size: 25px;
            margin-bottom: 0px;
            position: absolute;
            left: 40px;
            top: 0;
        }
        .label1_explain, .label2_explain, .label3_explain, .label4_explain{
            font-family: 'Gugi', cursive;
        }
        .label1_explain div{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 240px;
            margin-top:18px;
            border-radius: 50%;
            font-size: 20px;
        }
        .label1_explain div:last-child{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 0px;
        }
        .label1_explain p{
            display: inline-block;
            vertical-align: middle;
        }
        .label2_explain div{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 200px;
            margin-top:18px;
            border-radius: 50%;
            font-size: 20px;
        }
        .label2_explain div:last-child{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 0px;
        }
        .label2_explain p{
            display: inline-block;
            vertical-align: middle;
        }
        .age{
            position: relative;
            background-color: #E1FACD;
            height: 440px;
        }
        .label2{
            vertical-align: middle;
            display:inline-block; 
            background-color: rgba(255, 171, 45, 0.753); 
            width:300px; 
            color: white;
            text-align:center; 
            height: 60px;
            line-height: 60px;
            font-family: 'Gugi', cursive;
            font-size: 25px;
            margin-bottom: 0px;
            position: absolute;
            left: 40px;
            top: 0;
        }
        .with{
            position: relative;
            background-color: #D2FAD6;
            height: 440px;
        }
        .label3{
            vertical-align: middle;
            display:inline-block; 
            background-color: rgba(255, 171, 45, 0.753); 
            width:270px; 
            color: white;
            text-align:center; 
            height: 60px;
            line-height: 60px;
            font-family: 'Gugi', cursive;
            font-size: 25px;
            margin-bottom: 0px;
            position: absolute;
            left: 40px;
            top: 0;
        }
        .label3_explain div{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 260px;
            margin-top:18px;
            border-radius: 50%;
            font-size: 20px;
        }
        .label3_explain div:last-child{
            display: inline-block;
            width:100px;
            height:40px;
            line-height: 40px;
            background-color: rgb(15, 1, 77);
            color: white;
            margin-right: 0px;
        }
        .label3_explain p{
            display: inline-block;
            vertical-align: middle;
        }
        input[type="checkbox"] {
            display: none;
        }
        input[type="checkbox"]+label{
            display: inline-block;
            border-radius: 100%;
            cursor: pointer;
            transition: 0.3s;
        }
        input[type="checkbox"]+label:hover{
            transform:scale(1.2);
        }
        .gender input[type="checkbox"]+label{
            margin-top: 50px;
        }
        .age input[type="checkbox"]+label{
            margin-top: 60px;
        }
        .with input[type="checkbox"]+label{
            margin-top: 55px;
        }
        .theme_images input[type="checkbox"]+label{
            border-radius: 0%;
        }
        #man_check+label {
            margin-right: 100px;
            width: 240px;
            height: 300px;
            background: url('../../public/Select_Man.jpg') no-repeat 0 0px / contain;
        }
        #man_check:checked+label {
            background: url('../../public/Selected_Man.jpg') no-repeat 0 1px / contain;
        }
        #woman_check+label {
            width: 240px;
            height: 300px;
            background: url('../../public/Select_Woman.jpg') no-repeat 0 0px / contain;
        }
        #woman_check:checked+label {
            background: url('../../public/Selected_Woman.jpg') no-repeat 0 1px / contain;
        }
        #check_10th+label {
            margin-right: 20px;
            width: 280px;
            height: 280px;
            background: url('../../public/Select_10th.jpg') no-repeat 0 0px / contain;
        }
        #check_10th:checked+label {
            background: url('../../public/Selected_10th.jpg') no-repeat 0 1px / contain;
        }        
        #check_20th+label {
            margin-right: 20px;
            width: 280px;
            height: 280px;
            background: url('../../public/Select_20th.jpg') no-repeat 0 0px / contain;
        }
        #check_20th:checked+label {
            background: url('../../public/Selected_20th.jpg') no-repeat 0 1px / contain;
        }        
        #check_30th+label {
            margin-right: 20px;
            width: 280px;
            height: 280px;
            background: url('../../public/Select_30th.jpg') no-repeat 0 0px / contain;
        }
        #check_30th:checked+label {
            background: url('../../public/Selected_30th.jpg') no-repeat 0 1px / contain;
        }        
        #check_40th+label {
            margin-right: 20px;
            width: 280px;
            height: 280px;
            background: url('../../public/Select_40th.jpg') no-repeat 0 0px / contain;
        }
        #check_40th:checked+label {
            background: url('../../public/Selected_40th.jpg') no-repeat 0 1px / contain;
        }        
        #check_50th+label {
            width: 280px;
            height: 280px;
            background: url('../../public/Select_50th.png') no-repeat 0 0px / contain;
        }
        #check_50th:checked+label {
            background: url('../../public/Selected_50th.png.jpg') no-repeat 0 1px / contain;
        }
        #check_solo+label {
            width: 280px;
            height: 280px;
            margin-right: 80px;
            background: url('../../public/Select_solo.png') no-repeat 0 0px / contain;
        }
        #check_solo:checked+label {
            background: url('../../public/Selected_solo.jpg') no-repeat 0 1px / contain;
        }
        #check_couple+label {
            width: 280px;
            height: 280px;
            margin-right: 80px;
            background: url('../../public/Select_couple.jpg') no-repeat 0 0px / contain;
        }
        #check_couple:checked+label {
            background: url('../../public/Selected_couple.jpg') no-repeat 0 1px / contain;
        }
        #check_friends+label {
            width: 280px;
            height: 280px;
            margin-right: 80px;
            background: url('../../public/Select_friends.jpg') no-repeat 0 0px / contain;
        }
        #check_friends:checked+label {
            background: url('../../public/Selected_friends.jpg') no-repeat 0 1px / contain;
        }
        #check_family+label {
            width: 280px;
            height: 280px;
            background: url('../../public/Select_family.jpg') no-repeat 0 0px / contain;
        }
        #check_family:checked+label {
            background: url('../../public/Selected_family.jpg') no-repeat 0 1px / contain;
        }
        .theme_message{
            text-align: center; 
            height: 100px;
        }
        .theme_message h1{
            line-height: 100px;
            vertical-align: middle;
            font-family: 'Do Hyeon', sans-serif;
            background-color: #CFFAE1;
        }
        .theme_images{
            background-color: #D3F1F1;
        }
        .theme_images div{
            width: 200px;
            height: 400px;
            display: inline-block;
            overflow: hidden;
        }
        .theme_explain{
            background-color: #D7EBF0;
        }
        .theme_explain div{
            width: 200px;
            height: 100px;
            display: inline-block;
        }
        .theme_explain h1{
            line-height: 100px;
            vertical-align: middle;
            font-size: 30px;
            font-family: 'Gugi', cursive;
            color: #161616;
            font-weight: bold;
        }
        #check_nature+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_nature.jpg') no-repeat 0 0px / contain;
            overflow: hidden;
        }
        #check_nature:checked+label {
            background: url('../../public/theme/Selected_nature.jpg') no-repeat 0 1px / contain;
        }
        #check_park+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_park.jpg') no-repeat 0 0px / contain;
        }
        #check_park:checked+label {
            background: url('../../public/theme/Selected_park.jpg') no-repeat 0 1px / contain;
        }
        #check_culture+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_culture.jpg') no-repeat 0 0px / contain;
        }
        #check_culture:checked+label {
            background: url('../../public/theme/Selected_culture.jpg') no-repeat 0 1px / contain;
        }
        #check_shopping+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_shopping.jpg') no-repeat 0 0px / contain;
        }
        #check_shopping:checked+label {
            background: url('../../public/theme/Selected_shopping.jpg') no-repeat 0 1px / contain;
        }
        #check_interesting+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_interesting.jpg') no-repeat 0 0px / contain;
        }
        #check_interesting:checked+label {
            background: url('../../public/theme/Selected_interesting.jpg') no-repeat 0 1px / contain;
        }
        #check_history+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_history.jpg') no-repeat 0 0px / contain;
        }
        #check_history:checked+label {
            background: url('../../public/theme/Selected_history.jpg') no-repeat 0 1px / contain;
        }
        #check_walking+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_walk.jpg') no-repeat 0 0px / contain;
        }
        #check_walking:checked+label {
            background: url('../../public/theme/Selected_walk.jpg') no-repeat 0 1px / contain;
        }
        #check_experience+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_experience.jpg') no-repeat 0 0px / contain;
        }
        #check_experience:checked+label {
            background: url('../../public/theme/Selected_experience.jpg') no-repeat 0 1px / contain;
        }
        #check_festival+label {
            width: 200px;
            height: 500px;
            background: url('../../public/theme/Select_festival.jpg') no-repeat 0 0px / contain;
        }
        #check_festival:checked+label {
            background: url('../../public/theme/Selected_festival.jpg') no-repeat 0 1px / contain;
        }
        .submit{
            padding: 13px;
            font-size: 30px;
            opacity: 0.9;
            color:black;
            border-radius: 8px;
            background-color: #deadff;
            cursor: pointer;
            font-family: 'Do Hyeon', sans-serif;
            width: 400px;
            border:none;
        }
        .submit:hover{
            background-color: #ffc6ce;
        }
</style>