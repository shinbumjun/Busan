<template>
    <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
        <div class="carousel-inner">
            <div class="carousel-item active">
                <img src="../Img/Headbar_Busan_4.png" class="d-block w-100" >
                <div class="d-none d-md-block carousel_subtext">
                    <div class="name">
                        <p>추천 선택</p>
                        <p style="font-size: 30px;">Recommand Select</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default{

}
</script>

<style>
        .carousel-item img{
            height: 450px;
            filter: brightness(90%);
        }
        .carousel{
            margin: 60px 0px 0px 0px;
            z-index: 20;
        }
        .carousel_headtext{
            text-align: left;
            margin-bottom: 300px;
        }
        .carousel_headtext h1{
            font-family: 'Gugi', cursive;
            font-size: 60px;
        }
        .carousel_headtext p{
            font-family: 'Pacifico', cursive;
            font-size:25px;
        }
        .carousel_subtext{
            margin-bottom:20px;
            text-align: right;
        }
        .name{
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
        .name p:first-child{
            margin-bottom: 0px;
        }

</style>