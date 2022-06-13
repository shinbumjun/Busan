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
    <div class="box" style="height: 1700px;">
    <br>
    <h2 class="text-center">관광지</h2>
    <br>
    <BusanTouristspotList :list-array="items"></BusanTouristspotList>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
import BusanTouristspotList from './BusanTouristspotlist.vue';

export default {
 components: { BusanTouristspotList },
 data() {
     return {
         items: []
     }
 },
 created(){
     axios.get('/api/v1/touristspotslist/')
     .then((response) => this.items = response.data)
     .catch((err) => console.log(err))
 }
}
</script>

<style>

</style>