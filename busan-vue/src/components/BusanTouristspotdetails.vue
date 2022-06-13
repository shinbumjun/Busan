<template>
  <main>
    <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="https://cdn.pixabay.com/photo/2017/03/14/16/56/banner-2143727_1280.jpg" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>관광지</p>
                            <p style="font-size: 30px;">tourist attraction</p>
                        </div>
                    </div>
                </div>
            </div>
    </div>
    <div class="box" style="height: 2000px;">
    <div class="container">
        <h5 class="text-center text-primary my-3">부산시 관광 명소</h5>
        <h2 class="text-center mb-4">{{items.name}}</h2>
        <hr>
        <img :src="items.get_image" class="mt-3" alt="..." width=100%>
        <p class="my-4 border p-3 bg-light">{{items.description}}</p>
        <h4 class="text-center text-primary my-3">주소</h4>
        <p class="text-center my-3">{{items.address}}</p>
        <h5 class="text-primary mt-4">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tags-fill" viewBox="0 0 16 16">
                <path d="M2 2a1 1 0 0 1 1-1h4.586a1 1 0 0 1 .707.293l7 7a1 1 0 0 1 0 1.414l-4.586 4.586a1 1 0 0 1-1.414 0l-7-7A1 1 0 0 1 2 6.586V2zm3.5 4a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
                <path d="M1.293 7.793A1 1 0 0 1 1 7.086V2a1 1 0 0 0-1 1v4.586a1 1 0 0 0 .293.707l7 7a1 1 0 0 0 1.414 0l.043-.043-7.457-7.457z"/>
            </svg>
            연관 태그
        </h5>
        <div class="my-3">
            <span class="mx-2 text-black-50">#{{items.thema}}</span>
            <!-- <span class="mx-2 text-black-50">#자연</span><span class="mx-2 text-black-50">#이색여행</span> -->
        </div>
        <hr>
    </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
export default {
 data() {
     return {
         items: []
     }
 },
 created(){
     axios.get(`/api/v1/touristspot/${this.$route.params.id}/`)
     .then((response) => this.items = response.data)
     .catch((err) => console.log(err))
 },
}
</script>

<style>

</style>