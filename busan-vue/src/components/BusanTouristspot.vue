<template>
  <main>
    <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="https://p4.wallpaperbetter.com/wallpaper/140/352/958/gwangan-bridge-busan-south-korea-wallpaper-3840%C3%972400-wallpaper-preview.jpg" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>관광지</p>
                            <p style="font-size: 30px;">tourist attraction</p>
                        </div>
                    </div>
                </div>
            </div>
    </div>
    <div class="box" style="height: 2100px;">
    <br>
    <div style="vertical-align:center;">
    </div>
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