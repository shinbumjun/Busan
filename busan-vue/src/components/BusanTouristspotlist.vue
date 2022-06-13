<template>
    <div>
      <div class="container">
        <div class="row row-cols-1 row-cols-md-3 g-4">
            <div class="col" v-for="p in paginatedData" :key="p.id">
                <router-link to="/touristspotdetails">
                    <div class="card h-100">
                        <img :src="p.get_thumbnail" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">{{p.name}}</h5>
                            <p class="card-text">{{p.address}}</p>
                            <!-- <span class="badge text-bg-dark me-1" v-for="(t,i) in p.thema" :key="i">{{t}}</span> -->
                            <span class="badge text-bg-dark me-1">{{p.thema}}</span>
                            <!-- <span class="badge text-bg-dark me-1">이색여행</span> -->
                        </div>
                    </div>
                </router-link>
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
    }
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
    }
  },
//    created(){
//     let a = this.paginatedData()
//     console.log(a)
//  }
}
</script>

<style>

</style>