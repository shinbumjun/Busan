<template>
  <main>
    <div id="carouselExampleCaptions" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active head">
                    <img src="https://cdn.pixabay.com/photo/2020/03/12/14/24/busan-4925217_1280.jpg" class="d-block w-100" >
                    <div class="d-none d-md-block carousel_subtext">
                        <div class="subject">
                            <p>커뮤니티</p>
                            <p style="font-size: 30px;">community</p>
                        </div>
                    </div>
                </div>
            </div>
    </div>
    <div class="box" style="height: 1000px;">
      <div class="container">
        <br>
        <h2 class="text-center">커뮤니티 작성</h2>  
        <div>
            <div class="mb-3">
                <label class="form-label" for="title">제목</label>
                <input class="form-control" type="text" name="title" id="title" v-model="title"/>
            </div>
            <div class="mb-3">
                <label class="form-label" for="content">내용</label> 
                <textarea class="form-control"  name="content" id="content" v-model="content"></textarea>
            </div>
            <!-- <input type="hidden" id="token" name="token" :value="headers"> -->
            <button class="btn btn-outline-secondary btn-sm" type="submit" @click="regPosts()">저장</button>
        </div>
    </div>
    </div>
  </main>
</template>

<script>
import axios from 'axios';
export default {
  methods: {
    regPosts() {
      let params = {
        // "author": "vue",
        "title" : this.title,
        "content" : this.content,
      }
      axios.post('http://127.0.0.1:8000/api/v1/board/',
      JSON.stringify(params), {headers: { 'content-type':
      'application/json',
      // 나중에 받아올 토큰값을 적는다. 현재 임시로 test3의 토큰값을 적어놓음.
      'Authorization': 'token d548c2da5d0b412017c3bad825397d0427f8e956ff7d45c4b9b940d05976458d' 
      }}
      ).then(res => {
        alert("성공적으로 저장되었습니다.\nn글 번호 : [" + res.data + "]")
        this.$router.push("/community")
      }).catch(e => {
        // alert('e.response.data')
        alert(e+'실패')
      })
    }
  } 
}
</script>

<style>
  textarea {
    height: 20em;
  }
</style>