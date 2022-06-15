<template>
    <div>
      <div class="container" style="height:1650px;">
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div class="col" v-for="p in paginatedData" :key="p.id" >
              <div style="text-align: center;height: 500px; ">  
                <router-link :to="'/touristspotdetails/' + p.id">
                  <a class="card2">
                      <div>
                          <img :src="p.get_thumbnail" style="width: 410px; height: 300px;">
                      </div>
                      <div class="card2_explain">
                          <div></div>
                          <p>{{p.name}}</p>
                          <p style="font-weight: 0;font-size: 15px;">{{p.address}}</p>
                          <p style="font-weight: 0;font-size: 15px;">#{{p.thema}}</p>
                      </div>
                  </a> 
                    <!-- <div class=" h-100" style="width:410px; height:500px">
                        <img :src="p.get_thumbnail" class="card-img-top" alt="..." style="width:410px; height:300px;">
                        <div class="card-body">
                            <h5 class="card-title">{{p.name}}</h5>
                            <p class="card-text">{{p.address}}</p>-->
                            <!-- <span class="badge text-bg-dark me-1" v-for="(t,i) in p.thema" :key="i">{{t}}</span> -->
                         <!--   <span class="badge text-bg-dark me-1">{{p.thema}}</span> -->
                            <!-- <span class="badge text-bg-dark me-1">이색여행</span> -->
                        <!--</div>
                    </div>--> 
                </router-link>
              </div>
            </div>
        </div>
      </div>
        <br>
        <nav>
            <ul class="pagination justify-content-center">
                <li class="page-item">
                    <button class="page-link" :disabled="pageNum === 0" @click="prevPage" >Prev</button>
                </li>
                <li class="page-item active">
                    <p class="page-link">{{ pageNum + 1 }} / {{ pageCount }} 페이지</p>
                </li>
                <li class="page-item" >
                    <button class="page-link" :disabled="pageNum >= pageCount - 1" @click="nextPage" >Next</button>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
export default {
    name: 'BusanTouristspotList',
  data () {
    return {
      pageNum: 0
    }
  },
  props: {
    listArray: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 9
    }
  },
  methods: {
    nextPage () {
      this.pageNum += 1;
    },
    prevPage () {
      this.pageNum -= 1;
    },
    // jsonTrans() {
    //   let jthe = this.paginatedData ()
    //   console.log(jthe)
    //   // return jthe
    // }
  },
  computed: {
    pageCount () {
      let listLeng = this.listArray.length,
          listSize = this.pageSize,
          page = Math.floor(listLeng / listSize);
      if (listLeng % listSize > 0) page += 1;
      
      /*
      아니면 page = Math.floor((listLeng - 1) / listSize) + 1;
      이런식으로 if 문 없이 고칠 수도 있다!
      */
      return page;
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize,
            end = start + this.pageSize;
      return this.listArray.slice(start, end);
    },
    // jsonTrans() {
    //   let jthe = this.paginatedData
    //   return JSON.parse(jthe)
    // }
  },
//    created(){
//    jsonTrans();
//  }
}
</script>

<style>
        .col{
          margin-top: 0px;
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
        .card2{
            border: 2px solid rgb(124, 176, 255);
            width: 410px; 
            height: 460px; 
            display: inline-block; 
            margin-top: 100px; 
            text-decoration: none;
        }
        .card2_explain p{
            margin-top: 20px;
            margin-left: 20px;
            text-align: left;
            color: black;
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 20px;
            font-weight: 600;
        }
        .card2 div{
            overflow: hidden;
        }
        .col img:hover{
            transform: scale(1.2);
            transition: 0.3s;
        }
</style>