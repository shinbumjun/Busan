<template>
    <div id='wrap'>
        <footer>
            <div>
                <div style="width:45%; color: white; display: inline-block; text-align: left;">
                    <span class="white">(주) Busan For U</span><br />
                </div>
                <div style="width:45%; color: white; display: inline-block; text-align: right;">
                    <button class="but_logo">
                        <img src="../../../public/facebook-logo-icon.png">
                    </button>
                    <button class="but_logo">
                        <img src="../../../public/instagram-logo-icon.png">
                    </button>
                    <button class="but_logo">
                        <img src="../../../public/youtube-logo-icon.png">
                    </button>
                    <button class="but_logo">
                        <img src="../../../public//blog-black-icon.png">
                    </button>
                    <span style="font-size: 17px; margin-left: 20px;">부산관광문의 _</span>
                    <span style="font-size: 40px;color:cornflowerblue;font-weight: 1000;">4258</span>
                </div>
            </div>
            <div>

            </div>
            <div class="footer_end">
                <span class="gray">Fax : 02-1234-5678</span>
                <span style="margin-right:10px;margin-left:10px; font-weight: bold;">|</span>
                <span class="gray">E-mail : Acorn_team4@naver.com</span><br/>

                <span class="gray">고객센터 전화문의 080-987-6543</span>
                <span style="margin-right:10px;margin-left:10px; font-weight: bold;">|</span>
                <span class="gray">Copyright 2022. Team4. All Rights Reserved.</span>
            </div>
        </footer>
    </div>
</template>

<script>
export default{
    name : 'Main_footer'
}
</script>

<style>
        #wrap {
            min-height: 100%;
            position: relative;
            width: 100%;
            font-family: 'IBM Plex Sans KR', sans-serif;
        }

        footer {
            padding-top:20px;
            width: 100%;
            height: 240px; 
            bottom: 0;
            position: absolute;
            background-color: #161616;
            color:#666666;
            font-size:18px;
            text-align:center;
        }
        .white{
            color:white;
            font-size: 25px;
            font-weight: bold;
        }

        .gray{
            font-weight:bold;
            text-align:left;
        }
        .but_logo img{
            width: 30px;
            height: 30px;
        }
        .footer_end{
            margin-top: 30px;
            text-align: left; 
            margin-left: 70px; 
        }
        .footer_end span{
            font-size: 15px;
        }

</style>