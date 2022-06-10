<template>
    <div>
        <!-- Head IMG Part -->
        <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="/Headbar_Busan_5.png" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>추천결과</p>
                            <p style="font-size: 30px;">Recommand Result</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Content Part-->
        <div class="box2">
            <div class="content-top">
                <h1>선택한 정보에 따른 추천 여행지입니다.</h1>
            </div>
            <div class="result_top">
                <div class="selected_options">
                    <p style="margin-left: 15px;">{ }님이 선택하신 정보입니다.<br> 선택하신 {},{},{},{},{} 에 따른 여행지를 추천합니다.</p>
                </div>
            </div>
            <div class="result" style="background-color: #b7e9ff;">
                <div class="row" style="margin-left: 150px;margin-right: 150px;">
                    <div class="col">
                        <div style="text-align: center;height: 600px;">
                            <a class="card" href="">
                                <div>
                                    <img src="/Recommand_cheonghak.jpg" style="width: 290px; height: 230px;">
                                </div>
                                <div class="card_explain">
                                    <div></div>
                                    <p>청학 배수지 전망대</p>
                                    <p style="font-weight: 0;font-size: 15px;">부산광역시 영도구</p>
                                    <p style="font-weight: 0;font-size: 15px;"># 체험</p>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div class="col">
                        <div style="text-align: center;height: 600px;">
                            <a class="card" href="">
                                <div>
                                    <img src="/Recommand_yonggoongsa.jpg" style="width: 290px; height: 230px;">
                                </div>
                                <div class="card_explain">
                                    <div></div>
                                    <p>해동 용궁사</p>
                                    <p style="font-weight: 0;font-size: 15px;">부산광역시 기장군 기장읍</p>
                                    <p style="font-weight: 0;font-size: 15px;"># 역사</p>
                                </div>
                            </a>
                        </div>
                    </div>
                    <div class="col">
                        <div style="text-align: center;height: 600px;">
                            <a class="card" href="">
                                <div>
                                    <img src="/Recommand_hwangtoegill.jpg" style="width: 290px; height: 230px;">
                                </div>
                                <div class="card_explain">
                                    <div></div>
                                    <p>땅뫼산 황토길</p>
                                    <p style="font-weight: 0;font-size: 15px;">부산광역시 금정구</p>
                                    <p style="font-weight: 0;font-size: 15px;"># 자연</p>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

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
        .box2{
            height: 1200px;
            overflow: hidden;
            margin-left: 200px;
            margin-right: 200px;
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
        .result_top{
            position: relative;
            height: 120px; 
            background-color:#CDFAEF;
        }
        .selected_options{
            vertical-align: middle;
            display:inline-block; 
            width:1200px; 
            color: black;
            text-align:left; 
            height: 120px;
            line-height: 60px;
            font-family: 'Do Hyeon', sans-serif;
            font-size: 30px;
            margin-bottom: 0px;
            position: absolute;
            left: 40px;
            top: 0;
        }
        .card{
            border: 3px solid beige;
            width: 300px; 
            height: 420px; 
            display: inline-block; 
            margin-top: 100px; 
            text-decoration: none;
        }
        .card_explain p{
            margin-top: 20px;
            margin-left: 20px;
            text-align: left;
            color: black;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 20px;
            font-weight: 600;
        }
        .card div{
            overflow: hidden;
        }
        .col img:hover{
            transform: scale(1.2);
            transition: 0.3s;
        }
</style>